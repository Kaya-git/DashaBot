from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import main_menu
from utils import callbackdata
from aiogram import F
from finalstate.fsm import GarantStates
from aiogram.types import Message
from config import conf


garantinfologic = Router(name="Обращение по гарантии")


@garantinfologic.callback_query(callbackdata.GarantInfo.filter(
    F.garant_info == 'garant'
))
async def garantinfo(
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
        text="""Опишите Вашу проблему в ответном сообщении, и наш менеджер свяжется с Вами в течение суток.""",
        reply_markup=await main_menu()
    )).message_id)

    await state.set_state(GarantStates.problem_text)


@garantinfologic.message(GarantStates.problem_text)
async def problem_text(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete"]
        )

    await state.update_data(problem_text=message.text)

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=(await message.reply(
        text="""
        Благодарим Вас за обращение. Представитель скоро с Вами свяжется в личном сообщении. Убедитесь, что Вам возможно отправлять сообщения.
        """,
        reply_markup=await main_menu()
    )).message_id)

    data = await state.get_data()
    await conf.telegram.bot.send_message(
        chat_id=conf.chat_id,
        text=f"""
            Новое обращение:
            id: {data["client_telegram_id"]},
            username: {message.from_user.username}
            Message: {data["problem_text"]}
        """
    )
    await message.delete()
