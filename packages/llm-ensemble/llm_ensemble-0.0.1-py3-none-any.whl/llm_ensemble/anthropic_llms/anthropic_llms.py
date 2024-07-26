import anthropic
from typing import get_type_hints, get_args


def get_anthropic_models():
    tray_client = anthropic.Anthropic()
    model_param_type_hint = get_type_hints(tray_client.messages.create)
    models = get_args(get_args(model_param_type_hint["model"])[1])

    return models
