from aiogram import Bot, Dispatcher, types
import asyncio
from config import conf
import logging
from aiogram.filters import CommandStart
from logic.callback import part_number_router
from logic.back import back_router
from keyboards.inline import get_inline_keyboard


bot = Bot(token=conf.telegram.bot_token)
dp = Dispatcher()


dp.include_router(part_number_router)
dp.include_router(back_router)


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text="""Привет, модница!

Выбери артикул твоей сумочки в меню ниже, и мы пришлём для тебя несколько подходящих образов🤍""",
        reply_markup=get_inline_keyboard()
    )
    await message.delete()


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
