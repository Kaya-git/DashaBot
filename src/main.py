from aiogram import Dispatcher, types
import asyncio
from config import conf
import logging
from aiogram.filters import CommandStart
from logic.callback import part_number_router
from logic.smth_else import smth_else_router
from logic.back import back_router
from keyboards.inline import get_inline_keyboards


dp = Dispatcher()

dp.include_router(part_number_router)
dp.include_router(smth_else_router)
dp.include_router(back_router)

COUNT_USERS = 0


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    global COUNT_USERS
    COUNT_USERS += 1
    await conf.telegram.bot.send_message(
        378288967,
        f"Переход на бота! Общее кол-во переходов: {COUNT_USERS}"
    )
    await message.answer(
        text="""Привет!

Этот бот поможет тебе решить вопросы по гарантии на наш товар. Обязательно опробуй нашу игру по кнопке снизу и забери свой приз!""",
        reply_markup=get_inline_keyboards.get_main_inline_keyboard()
    )
    await message.delete()


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(conf.telegram.bot)


if __name__ == "__main__":
    asyncio.run(main())
