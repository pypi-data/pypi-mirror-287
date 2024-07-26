import os
import anthropic
from anthropic.types import MessageParam
from typing import List, Optional, TypedDict, Iterable, Literal
from typing_extensions import Required

from ..llm_models import base_llms
from ..shared import MessageDict


class ClaudeParameterDict(TypedDict, total=False):
    temperature: Required[float]
    max_tokens: int


class ClaudeClient:
    def __init__(
        self,
        name: str,
        sentiment_prompt: Optional[str] = None,
        model: Optional[str] = None,
        parameter: Optional[ClaudeParameterDict] = None,
        api_key: str = os.environ.get("ANTHROPIC_API_KEY"),
    ):
        parameter = {} if not parameter else parameter
        model = model if model else base_llms.get("anthropic").get("primary_model")
        setup = {
            "model": model,
            "system": sentiment_prompt,
            "max_tokens": parameter.get("max_tokens", 1024),
            "temperature": parameter.get("temperature"),
        }

        self.name = name
        self.model = model if model else base_llms.get("anthropic").get("primary_model")

        self.client = anthropic.Anthropic(api_key=api_key)
        self.kwargs = {key: value for key, value in setup.items() if value}

    def answer_prompt(self, messages: Iterable[MessageParam]):
        request = self.client.messages.create(
            messages=messages,
            **self.kwargs,
        )

        prompt_answer = request.content[0].text
        return prompt_answer

    def answer(self, prompt: str):
        messages_list = self.convert_messages([MessageDict(user=prompt)])
        return self.answer_prompt(messages_list)

    def answer_conversation(self, conversation: List[MessageDict]):
        messages_list = self.convert_messages(conversation)
        return self.answer_prompt(messages_list)

    def answer_questionnaire(self, prompts: List[str]):
        conversation = []
        for prompt in prompts:
            conversation.append(MessageDict(user=prompt))
            current_answer = self.answer_conversation(conversation)
            conversation.append(MessageDict(ai=current_answer))

        return conversation[-1].get("ai"), conversation

    @staticmethod
    def convert_messages(
        message_list: List[MessageDict],
    ) -> Iterable[MessageParam]:
        def role_map(role: str) -> Literal["user", "assistant"]:
            if role == "user":
                return "user"
            elif role == "ai":
                return "assistant"
            else:
                raise ValueError('Parameter role must be one of ["user", "ai"].')

        converted_messages = [
            MessageParam(role=role_map(role), content=content)
            for message in message_list
            for role, content in message.items()
        ]

        return converted_messages
