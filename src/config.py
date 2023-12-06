import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class TelegramBot:
    bot_token = os.environ.get("BOT_TOKEN")


@dataclass
class Configuration:
    telegram = TelegramBot()


conf = Configuration()
