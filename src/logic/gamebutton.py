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

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            query.message.chat.id,
            data["message_to_delete"]
        )

    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=(await query.message.answer(
        text="""
        К сожалению, мы пока не умеем писать игры, но зато по этой кнопке мы спрятали для Вас сюрприз!
        """
    )).message_id)

    await sleep(1)

    data = await state.get_data()

    await state.set_state(GarantStates.message_to_delete_2)

    await state.update_data(message_to_delete_2=(await query.message.answer(
        text="""
        Оставьте отзыв на ВБ, и получите кэшбэк 150₽ на карту! Пришлите в ответном сообщении скриншот с отзывом.
        """,
        reply_markup=await main_menu()
    )).message_id)


@minigame_router.message(F.photo, ~F.caption)
async def screenshot(
    message: Message,
    state: FSMContext,
):
    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete"]
        )

    if "message_to_delete_2" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete_2"]
        )

    await state.set_state(GarantStates.screen_shot)
    await state.update_data(screenshot=message.photo[-1].file_id)

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=(await message.answer(
        text="""
        Благодарим за отзыв. Напишите реквизиты для перевода в формате "номер телефона, наименование банка" ,либо "номер банковской карты, наименование банка"
        """,
        reply_markup=await main_menu()
    )).message_id)
    await state.set_state(GarantStates.requisites)
    await message.delete()


@minigame_router.message(GarantStates.requisites)
async def cellphonerequest(
    message: Message,
    state: FSMContext
):

    await state.update_data(requisites=message.text)

    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete"]
        )

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=(await message.answer(
        text="""
        Благодарим Вас, деньги скоро поступят по указанным реквизитам. Наш администратор пришлет Вам квитанцию о переводе. Удостоверьтесь, что у Вас открытый аккаунт.
        """,
        reply_markup=await main_menu()
    )).message_id)

    data = await state.get_data()

    await conf.telegram.bot.send_message(
        chat_id=conf.chat_id,
        text=f"""
            Новый отзыв:
            id: {data["client_telegram_id"]},
            username: {message.from_user.username}
            Requisties: {data["requisites"]}
        """
    )
    await conf.telegram.bot.send_photo(
        chat_id=conf.chat_id,
        photo=data["screenshot"]
    )

    await message.delete()
