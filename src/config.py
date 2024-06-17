import os
from dataclasses import dataclass
from dotenv import load_dotenv
from aiogram import Bot


load_dotenv()


@dataclass
class TelegramBot:
    bot_token = os.environ.get("BOT_TOKEN")
    bot = Bot(token=bot_token)


@dataclass
class Configuration:
    chat_id = os.environ.get("CHAT_ID")
    prev_reply = None
    telegram = TelegramBot()


conf = Configuration()
