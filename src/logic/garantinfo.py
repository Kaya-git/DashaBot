from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline import get_main_inline_keyboard, main_menu
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
    await data["message_to_delete"].delete()

    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=await query.message.answer(
        text="""Опишите вашу проблему в ответном сообщении, и наш менеджер свяжется с вами в течение суток.""",
        reply_markup=await main_menu()
    ))

    await state.set_state(GarantStates.problem_text)


@garantinfologic.message(GarantStates.problem_text)
async def problem_text(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await state.update_data(problem_text=message.text)

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=await message.reply(
        text="""
        Благодарим вас за обращение. Представитель скоро с вами свяжется в личном сообщении. Убедитесь, что вам возможно отправлять сообщения.
        """,
        reply_markup=await get_main_inline_keyboard()
    ))

    data = await state.get_data()
    await conf.telegram.bot.send_message(
        378288967,
        f"""
            Новое обращение:
            id: {data["client_telegram_id"]},
            username: {message.from_user.username}
            Message: {data["problem_text"]}
        """
    )
    await message.delete()
