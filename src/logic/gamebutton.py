from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from asyncio import sleep
from keyboards.inline import get_inline_keyboard
from utils import callbackdata
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
    callback: callbackdata.MiniGame,
    state: FSMContext,
    message: Message
):

    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await message.reply(
        text="""
        К сожалению, мы пока не умеем писать игры,
        но зато по этой кнопке мы спрятали для тебя сюрприз!
        """
    )
    await sleep(5)

    await message.delete()

    await message.reply(
        text="""
        Оставь отзыв на ВБ, и получи кэшбэк 150₽ на карту!
        Пришли в ответном сообщении скриншот с отзывом,
        и наш менеджер свяжется с тобой для получения кэшбэка
        """
    )

    await state.set_state(GarantStates.screen_shot)


@minigame_router.message(GarantStates.screen_shot)
async def screenshot(
    message: Message,
    state: FSMContext,
):
    file_id = message.document.file_id

    file = await conf.telegram.bot.get_file(file_id)
    file_path = file.file_path

    await state.update_data(screen_shot=file_path)

    await conf.telegram.bot.send_message(
        378288967,
        f"""
            Новый отзыв:
            id: {state.client_telegram_id},
            Message: {state.file_path}
        """
    )
    await state.clear()
    await sleep(5)
    await message.delete()
