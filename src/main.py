from aiogram import Dispatcher, types
import asyncio
from config import conf
import logging
from aiogram.filters import CommandStart
from logic.gamebutton import minigame_router
from logic.garant6months import garant6months_router
from logic.garantinfo import garantinfologic
from logic.smth_else import smth_else_router
from logic.back import back_router
from keyboards.inline import get_main_inline_keyboard
from finalstate.fsm import GarantStates
from aiogram.fsm.context import FSMContext


dp = Dispatcher()

dp.include_router(minigame_router)
dp.include_router(garant6months_router)
dp.include_router(garantinfologic)
dp.include_router(smth_else_router)
dp.include_router(back_router)

COUNT_USERS = 0


@dp.message(CommandStart())
async def handle_start(message: types.Message, state: FSMContext):

    global COUNT_USERS
    COUNT_USERS += 1
    await conf.telegram.bot.send_message(
        378288967,
        f"Переход на бота! Общее кол-во переходов: {COUNT_USERS}"
    )

    await state.set_state(GarantStates.message_to_delete)
    md = await message.answer(
        text="""Привет!
Этот бот поможет тебе оформить гарантию на свой товар, либо обратиться по гарантийному случаю. Обязательно опробуй нашу игру по кнопке снизу и забери свой приз!
        """,
        reply_markup=await get_main_inline_keyboard()
    )
    await state.update_data(message_to_delete=md)

    await message.delete()


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(conf.telegram.bot)


if __name__ == "__main__":
    asyncio.run(main())
