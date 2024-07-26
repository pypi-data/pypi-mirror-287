from typing import TypedDict


class MessageDict(TypedDict, total=False):
    user: str
    ai: str
