from typing import Optional, Union, List
import concurrent.futures

from .anthropic_llms.anthropic_llm_wrapper import (
    ClaudeClient,
    ClaudeParameterDict,
)

from .openai_llms.openai_llm_wrapper import (
    ChatGPTClient,
    ChatGPTParameterDict
)

from .llm_models import BaseLlmsType, base_llms
from .llm_type import LlmsType

BASE_LLMS = [base_llms.get(x).get("primary_model") for x in base_llms.keys()]

# Bold console print
BSTART = "\033[1m"
BEND = "\033[0;0m"


def answer_questionnaire_llm_wrapper(arguments):
    llm = arguments[0]
    prompts = arguments[1]
    print_answer = arguments[2]
    print_conversation = arguments[3]

    return answer_questionnaire_llm(llm, prompts, print_answer, print_conversation)


def format_llm_name_str(llm_name: str) -> str:
    return f"\n-----\n{BSTART}{llm_name}:{BEND}"


def answer_questionnaire_llm(
        llm: LlmsType,
        prompts: List[str],
        print_answer: bool = False,
        print_conversation: bool = False,
):
    answer, conversation = llm.answer_questionnaire(prompts=prompts)

    if print_answer | print_conversation:
        print(format_llm_name_str(llm.name))

    if print_answer:
        print(answer)

    if print_conversation:
        print(conversation)

    return answer, conversation


class LLMs:
    def __init__(
        self,
        openai_key: str = None,
        anthropic_key: str = None,
        google_gemini_key: str = None,
    ) -> None:
        self.openai_key = openai_key
        self.anthropic_key = anthropic_key
        self.google_gemini_key = google_gemini_key

        self.llm_instances = dict()

    def initialize_defaults(self):
        if self.openai_key:
            client_name = "ChatGPT (Default)"
            parameter_dict = ChatGPTParameterDict(
                temperature=0,
            )
            hyperparameter = dict(parameter_dict)
            hyperparameter.update({"sentiment_prompt": None})

            llm_client = {
                "client": ChatGPTClient(name=client_name, api_key=self.openai_key, parameter=parameter_dict),
                "hyperparameter": hyperparameter,
                "base_model": base_llms.get("openai").get("primary_model"),
            }

            if self.llm_instances.get(client_name):
                print("Default ChatGPT client already instantiated.")
            else:
                self.llm_instances.update({client_name: llm_client})

        if self.anthropic_key:
            client_name = "Claude (Default)"
            parameter_dict = ClaudeParameterDict(
                temperature=0,
                max_tokens=1024,
            )
            hyperparameter = dict(parameter_dict)
            hyperparameter.update({"sentiment_prompt": None})

            llm_client = {
                "client": ClaudeClient(name=client_name, api_key=self.anthropic_key, parameter=parameter_dict),
                "hyperparameter": hyperparameter,
                "base_model": base_llms.get("anthropic").get("primary_model"),
            }

            if self.llm_instances.get(client_name):
                print("Default Claude client already instantiated.")
            else:
                self.llm_instances.update({client_name: llm_client})

        if self.google_gemini_key:
            print("Gemini client not implemented!")

    def initialize_llm(
        self,
        base_llm: Union[str, BaseLlmsType],
        client_name: str,
        api_key: str,
        sentiment_prompt: Optional[str] = None,
        parameter: Optional[Union[ClaudeParameterDict, ChatGPTParameterDict]] = None,
    ):
        if base_llm in base_llms.get("anthropic", {}).get('models', []):
            client = ClaudeClient(
                name=client_name,
                model=base_llm,
                sentiment_prompt=sentiment_prompt,
                parameter=parameter,
                api_key=api_key,
            )

        elif base_llm in base_llms.get('openai', []).get('models', []):
            client = ChatGPTClient(
                name=client_name,
                model=base_llm,
                sentiment_prompt=sentiment_prompt,
                parameter=parameter,
                api_key=api_key
            )

        else:
            raise ValueError(f"Model {base_llm} is not implemented yet.")

        if parameter:
            hyperparameter = dict(parameter)
        else:
            hyperparameter = {}
        hyperparameter.update({"sentiment_prompt": sentiment_prompt})

        llm_client = {
            "client": client,
            "hyperparameter": hyperparameter,
            "base_model": base_llm,
        }

        if self.llm_instances.get(client_name):
            print("Default Claude client already instantiated.")
        else:
            self.llm_instances.update({client_name: llm_client})

    def answer(self, prompt: str):
        for llm in self.llm_instances.keys():
            llm_client = self.llm_instances[llm].get("client")
            answer = llm_client.answer(prompt)
            print(format_llm_name_str(llm))
            print(answer)

    def answer_questionnaire(self, prompts: List[str], print_answer: bool = False, print_conversation: bool = False):
        answers = []
        for llm in self.llm_instances.keys():
            llm_client = self.llm_instances[llm].get("client")

            answer, _ = answer_questionnaire_llm(llm_client, prompts, print_answer, print_conversation)

            answers.append({llm: answer})

        return answers

    def answer_questionnaire_parallel(self, prompts: List[str], print_answer: bool = False, print_conversation: bool = False):

        llm_questionnaire_arguments = tuple(
            (self.llm_instances[x].get('client'), prompts, print_answer, print_conversation)
            for x in self.llm_instances.keys()
        )

        answers = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            threaded_answering = {executor.submit(answer_questionnaire_llm_wrapper, arguments): arguments for arguments in llm_questionnaire_arguments}
            for call_tread in concurrent.futures.as_completed(threaded_answering):

                answer = call_tread.result()
                answers.append(answer[0])

        return answers
