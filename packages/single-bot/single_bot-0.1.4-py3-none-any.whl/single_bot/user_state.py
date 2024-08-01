import asyncio
from single_bot.data_types import Message
import inspect


class UserState:
    def __init__(self, first_node: callable, user_state_dict: dict = None):
        if user_state_dict:
            self.__input_field = user_state_dict["input_template"]["input_field"]
            self.__button = user_state_dict["input_template"]["buttons"]
            self.__values = user_state_dict["values"]
        else:
            self.__input_field = {"node": first_node}
            self.__button = {}
            self.__values = {}
        self.__answers = [[]]
        self.__answer_pointer = 0
        self.__next_node = None
        self.__requested_values = {}
        self.__finish = False
        self.__node_counter = 0
        self.__current_node = None

        # "__actions" - the way to send system messeges to the bot
        # "__updates" - the way to send answers to UserState
        self.__actions = []
        self.__updates = {}

    def _get_user_state_dict(self):
        return {
            "input_template": {
                "input_field": self.__input_field,
                "buttons": self.__button,
            },
            "values": self.__values,
        }

    async def _invoke(self, request: Message):
        self.__user_request = request
        self.__node_counter = 0
        task = asyncio.create_task(self.__execute_nodes())
        async for response in self.__listen_messages():
            yield response
        self.__answers = [[]]
        self.__answer_pointer = 0
        self.__next_node = None
        return

    async def _update(self, values: dict):
        self.__updates.update(values)

    async def __execute_nodes(self):
        while True:

            node = self.__get_next_node()

            # await asyncio.sleep(0)
            if not node:
                self.__finish = True
                break
            self.__current_node = node.__name__
            self.__requested_values = {}
            self.__node_counter += 1
            if inspect.iscoroutinefunction(node):
                await node(self)
            else:
                node(self)

    def __get_next_node(self) -> callable:
        # Returns node for executing.

        if self.__node_counter == 0:
            for button in self.__button.keys():
                if button == self.__user_request["text"]:
                    node = self.__button[button]
                    self.__button = {}
                    return node
            self.__button = {}
            if "node" in self.__input_field.keys():
                if "validator" in self.__input_field.keys():
                    if self.__input_field["validator"](self.__user_request):
                        node = self.__input_field["node"]
                        self.__input_field = {}
                        return node
                    else:
                        return False

                node = self.__input_field["node"]
                self.__input_field = {}
                return node
        else:
            if self.__next_node:
                node = self.__next_node
                self.__next_node = None
                return node

        return False

    async def __listen_messages(self):
        self.__answer_counter = 0
        while True:
            await asyncio.sleep(0)
            # "__actions" - the way to send system messeges to the bot
            if len(self.__actions) != 0:
                yield self.__actions.pop(0)
            if self.__answer_counter < len(self.__answers):
                self.__answer_counter += 1
                yield {
                    "message": {
                        "text": self.__listen_streaming(self.__answer_counter - 1),
                        "buttons": list(self.__button.keys()),
                    },
                    "node": self.__current_node,
                    "requested_values": self.__requested_values,
                }

            elif self.__finish:
                break

    async def __listen_streaming(self, answer_id):
        chunk_counter = 0
        while answer_id == self.__answer_pointer or chunk_counter < len(
            self.__answers[answer_id]
        ):

            await asyncio.sleep(0)
            try:

                chunk = self.__answers[answer_id][chunk_counter]
                chunk_counter += 1
                yield chunk
            except:
                pass

    ### Methods for using in nodes
    def get_request(self) -> Message:
        return self.__user_request

    def send_message(self, text: str = "", stream: bool = False):
        try:
            self.__answers[self.__answer_pointer].append(text)
        except:
            self.__answers.append([])
            self.__answers[self.__answer_pointer].append(text)
        if not stream:
            self.__answer_pointer += 1
        if text == "":
            self.__answer_pointer += 1

    def add_button(self, name: str, node: callable):
        self.__button[name] = node

    def set_input_field(self, node):
        self.__input_field = {"node": node}

    def set_next_node(self, node):
        self.__next_node = node

    def set_value(self, name, value):
        self.__values[name] = value

    def get_value(self, name):
        try:
            value = self.__values[name]
        except:
            value = None
        # For creating history of values
        self.__requested_values[name] = value
        return value

    async def auth_check(self) -> bool:
        self.__actions.append("auth_check")
        while True:
            await asyncio.sleep(0)
            if "auth_check" in self.__updates.keys():
                return self.__updates.pop("auth_check")
