from aiogram import F, Router
from keyboards.inline import get_main_inline_keyboard
from aiogram.fsm.context import FSMContext
from finalstate.fsm import GarantStates
from utils import callbackdata
from aiogram.types import CallbackQuery
from config import conf

back_router = Router(name="back")


@back_router.callback_query(callbackdata.MenuRequest.filter(
    F.menu == "menu"
))
async def menu(query: CallbackQuery, state: FSMContext):

    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            query.message.chat.id,
            data["message_to_delete"]
        )

    if "message_to_delete_2" in data:
        await conf.telegram.bot.delete_message(
            query.message.chat.id,
            data["message_to_delete_2"]
        )

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=(await query.message.answer(
        text="""
            Этот бот поможет Вам решить вопросы по гарантии на наш товар. Обязательно опробуйте нашу игру по кнопке снизу и заберите свой приз!
        """,
        reply_markup=await get_main_inline_keyboard()
    )).message_id)
