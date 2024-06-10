from aiogram import F, Router
from keyboards.inline import get_main_inline_keyboard
from aiogram.fsm.context import FSMContext
from finalstate.fsm import GarantStates
from utils import callbackdata
from aiogram.types import CallbackQuery

back_router = Router(name="back")


@back_router.callback_query(callbackdata.MenuRequest.filter(
    F.menu == "menu"
))
async def menu(query: CallbackQuery, state: FSMContext):

    data = await state.get_data()
    data["message_to_delete"].delete()

    # current_state = await state.get_state()
    # if current_state is not None:
    #     await state.clear()

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=await query.message.answer(
        text="""
            Этот бот поможет тебе решить вопросы по гарантии на наш товар.
            Обязательно опробуй нашу игру по кнопке снизу и забери свой приз!
        """,
        reply_markup=await get_main_inline_keyboard()
    ))
    await query.message.delete()
