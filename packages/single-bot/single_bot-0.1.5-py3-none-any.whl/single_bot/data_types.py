from typing import TypedDict, Optional


class Message(TypedDict):
    text: str
    files: Optional[dict]


class MessengerRequest(TypedDict):
    messenger_name: str
    messenger_user_id: str
    authorized: bool
    message: Message


class InputField(TypedDict):
    node: callable
    validator: Optional[callable]
    description: Optional[str]


class InputTemplate(TypedDict):
    input_field: Optional[InputField]
    buttons: dict


class UserStateDict(TypedDict):
    input_template: InputTemplate
    values: Optional[dict]


class RequestedData(TypedDict): ...


class History(TypedDict):
    node: str
    position_in_node: int
    requested_values: dict
    question: str
    answer: str
