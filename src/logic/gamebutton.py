from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from asyncio import sleep
from utils import callbackdata
from keyboards.inline import main_menu
from aiogram import F
from finalstate.fsm import GarantStates
from aiogram.types import Message
from config import conf


minigame_router = Router(name="Мини Игра")


@minigame_router.callback_query(callbackdata.MiniGame.filter(
    F.mini_game == "mini_game"
))
async def minigame(
    query: CallbackQuery,
    state: FSMContext
):

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=await query.message.answer(
        text="""
        К сожалению, мы пока не умеем писать игры,
        но зато по этой кнопке мы спрятали для тебя сюрприз!
        """
    ))

    await sleep(5)

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=await query.message.answer(
        text="""
        Оставь отзыв на ВБ, и получи кэшбэк 150₽ на карту!
        Пришли в ответном сообщении скриншот с отзывом,
        и наш менеджер свяжется с тобой для получения кэшбэка
        """,
        reply_markup=await main_menu()
    ))


@minigame_router.message(F.photo, ~F.caption)
async def screenshot(
    message: Message,
    state: FSMContext,
):
    data = await state.get_data()
    await data["message_to_delete"].delete()

    await conf.telegram.bot.send_message(
        chat_id=378288967,
        text=f"Новый отзыв от: {data["client_telegram_id"]}"
    )
    await conf.telegram.bot.send_photo(
        chat_id=378288967,
        photo=message.photo[-1].file_id
    )
    await state.set_state(GarantStates.screen_shot)
    await state.update_data(screenshot=message.photo[-1].file_id)

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=await message.answer(
        text="""
        Благодарим за отзыв.
        Наш менеджер скоро свяжется с вами.
        Удостоверьтесь, что у вас открыта личка.
        """,
        reply_markup=await main_menu()
    ))

    await message.delete()
