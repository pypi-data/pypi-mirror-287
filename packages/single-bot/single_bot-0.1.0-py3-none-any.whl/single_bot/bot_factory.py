from single_bot.messengers import TelegramBot, CmdBot
from single_bot.user_id_storage import UserIdStorage
from single_bot.user_state_storage import UserStateStorage
from single_bot.bot import Bot
from typing import Literal


class BotFactory:
    # Responsible for creating and starting messengers
    def __init__(self, first_node):
        self.bot = Bot(UserIdStorage(), UserStateStorage(), first_node=first_node)

    async def start(self, platform: Literal["telegram", "cmd"]):
        if platform == "telegram":
            messenger = TelegramBot(self.bot)
            await messenger.run()
        if platform == "cmd":
            messenger = CmdBot(self.bot)
            await messenger.run()
