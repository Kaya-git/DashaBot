from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from asyncio import sleep
from keyboards.inline import get_inline_keyboards
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
    state: FSMContext,
    callback: callbackdata.GarantInfo,
    message: Message
):
    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.problem_text)

    await message.answer(
        text="Опишите вашу проблему в ответном сообщении, и наш менеджер свяжется с вами в течение суток."
    )
    await message.delete()


@garantinfologic.message(GarantStates.problem_text)
async def problem_text(
    message: Message,
    state: FSMContext
):
    await state.update_data(problem_text=message.text)
    await message.reply(
        text="Благодарим вас за обращение. Представитель скоро с вами свяжется",
        reply_markup=get_inline_keyboards.get_main_inline_keyboard()
    )

    await conf.telegram.bot.send_message(
        378288967,
        f"""
            Новое обращение:
            id: {state.client_telegram_id},
            Message: {state.problem_text}
        """
    )

    await state.clear()
    await sleep(5)
    await message.delete()
