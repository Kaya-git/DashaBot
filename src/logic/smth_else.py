from aiogram import Router, types
from finalstate.fsm import GarantStates
from aiogram.fsm.context import FSMContext
from keyboards.inline import main_menu
smth_else_router = Router(name="smth_else")


@smth_else_router.message()
async def smt_else(message: types.Message, state: FSMContext):

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await message.delete()

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(await message.answer(
        text="Прости, но ты не можешь писать сюда сообщения",
        reply_markup=await main_menu()
    ))
