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
class RedisConfig:
    """ Redis connection variables"""

    db: str = int(os.environ.get("REDIS_DATABASE", 1))
    host: str = os.environ.get("REDIS_HOST")
    port: str = os.environ.get("REDIS_PORT")
    state_ttl: int = os.environ.get("REDIS_TTL_STATE", None)
    data_ttl: int = os.environ.get("REDIS_TTL_DATA", None)


@dataclass
class Configuration:
    chat_id = os.environ.get("CHAT_ID")
    prev_reply = None
    telegram = TelegramBot()
    redis = RedisConfig()


conf = Configuration()
