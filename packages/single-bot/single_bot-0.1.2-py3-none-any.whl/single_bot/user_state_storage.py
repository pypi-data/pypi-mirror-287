from single_bot.data_types import UserStateDict
from sqlitedict import SqliteDict
from typing import Union
import os


class UserStateStorage:
    def __init__(self):
        os.makedirs("data/", exist_ok=True)
        self.storage = SqliteDict("data/user_states.db", autocommit=True)

    def get_user_state(self, user_id: int) -> Union[UserStateDict, False]:
        user_id = str(user_id)
        if user_id in self.storage.keys():
            return self.storage[user_id]
        else:
            return False

    def save_user_state(self, user_id: int, state: UserStateDict):
        user_id_str = str(user_id)
        self.storage[user_id_str] = state
