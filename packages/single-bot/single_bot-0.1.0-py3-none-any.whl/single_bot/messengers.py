from aiogram import types, Bot, Dispatcher
from aiogram.types import Message
from single_bot.bot import Bot as ChatBot
import os
import dotenv
import asyncio


class TelegramBot:
    def __init__(self, bot: ChatBot):

        print(dotenv.get_key(dotenv.find_dotenv(), "TELEGRAM_TOKEN"))
        self.telegram_bot = Bot(dotenv.get_key(dotenv.find_dotenv(), "TELEGRAM_TOKEN"))
        self.chat_bot = bot
        self._create_dispatcher()

    async def run(self):

        import logging
        import sys

        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await self.dp.start_polling(self.telegram_bot)

    def _create_buttons(self, buttons=None):
        kb = [[]]
        for button in buttons:
            kb[0].append(types.KeyboardButton(text=button))
        return kb

    def _create_dispatcher(self):

        self.dp = Dispatcher()

        @self.dp.message()
        async def message_handler(message: Message):
            async def send_message(text, reply_markup):
                if len(text) > 4096:
                    for x in range(0, len(text), 4096):
                        await message.answer(message.chat.id, text[x : x + 4096])
                else:
                    await message.answer(message.chat.id, text)

            request = {
                "messenger_id": "telegram",
                "messenger_uid": message.from_user.id,
                "autorized": True,
                "request": {"text": message.text, "files": {}},
            }

            async for answer in self.chat_bot.get_answer(request):
                kb = [[]]
                text = await self._process_streaming(answer["text"])
                if "buttons" in answer.keys() and answer["buttons"]:
                    kb = self._create_buttons(answer["buttons"])
                    keyboard = types.ReplyKeyboardMarkup(
                        keyboard=kb, resize_keyboard=True
                    )
                    if len(text) > 4095:
                        for x in range(0, len(text), 4095):
                            await message.answer(
                                text[x : x + 4095], reply_markup=keyboard
                            )
                    else:
                        message = await message.answer(text, reply_markup=keyboard)

                else:
                    if len(text) > 4095:
                        for x in range(0, len(text), 4095):
                            await message.answer(
                                text[x : x + 4095],
                                reply_markup=types.ReplyKeyboardRemove(),
                            )
                    else:
                        message = await message.answer(
                            text, reply_markup=types.ReplyKeyboardRemove()
                        )

    async def _process_streaming(self, stream):
        answer = ""
        async for token in stream:
            answer += token
        return answer

    # @dp.message(F.contact)
    # async def contacts(message: Message):
    #     save_user_phone(message.from_user.id, message.contact.phone_number)
    #     await message.answer("Спасибо!")
    #     await message.answer(
    #         text="Добро пожаловать!\n\nТеперь бот в твоём распоряжении.\nЗадавай вопрос, связанный с ТК РФ:",
    #         reply_markup=types.ReplyKeyboardRemove(),
    #     )


class CmdBot:
    def __init__(self, bot: ChatBot):
        self.bot = bot

    async def run(self):

        while True:

            question = input("> ")
            request = {
                "messenger_id": "cmd",
                "messenger_uid": os.getlogin(),
                "request": {"text": question, "files": {}},
            }

            async for message in self.bot.get_answer(request):
                async for token in message["text"]:
                    print(token, end="")
                print("\n", end="")
                buttons = message["buttons"]
            for button in buttons:
                print(f" - {button}")


# class VkBot:
#     def __init__(self, bot: ChatBot):
#         self.bot = bot

#     async def run(self):
