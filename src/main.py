from aiogram import Bot, Dispatcher, types
import asyncio
from config import conf
import logging
from keyboards import kb_main_menu
from aiogram.filters import CommandStart
from logic.part_number import part_number_router
from logic.back import back_router


bot = Bot(token=conf.telegram.bot_token)
dp = Dispatcher()


dp.include_router(part_number_router)
dp.include_router(back_router)


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text="""Привет, модница!

Выбери артикул твоей сумочки в меню ниже,
и мы пришлём для тебя несколько подходящих образов🤍""",
        reply_markup=kb_main_menu
    )


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
