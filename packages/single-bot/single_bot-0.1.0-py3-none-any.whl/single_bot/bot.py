from single_bot.user_id_storage import UserIdStorage
from single_bot.user_state import UserState
from single_bot.user_state_storage import UserStateStorage
from single_bot.message_storage import MessageStorage
from single_bot.data_types import MessengerRequest


class Bot:
    # Responsible for managing users from messengers and running and saving their states.
    def __init__(
        self,
        user_id_storage: UserIdStorage,
        user_state_storage: UserStateStorage,
        first_node: callable,
    ):
        self.user_id_storage = user_id_storage
        self.first_node = first_node
        self.user_state_storage = user_state_storage

    async def get_answer(self, messenger_request: MessengerRequest):

        user_id = self.user_id_storage.get_user_id(
            messenger_request["messenger_id"], messenger_request["messenger_uid"]
        )
        user_state_dict = self.user_state_storage.get_user_state(user_id)

        if not user_state_dict:
            user_state = UserState(self.first_node)
        else:
            user_state = UserState(self.first_node, user_state_dict)

        async for message in user_state._invoke(messenger_request["request"]):
            yield message
        self.user_state_storage.save_user_state(
            user_id, user_state._get_user_state_dict()
        )
