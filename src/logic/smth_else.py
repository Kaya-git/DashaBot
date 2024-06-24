from aiogram import Router, types
from finalstate.fsm import GarantStates
from aiogram.fsm.context import FSMContext
from keyboards.inline import main_menu
from config import conf


smth_else_router = Router(name="smth_else")


@smth_else_router.message()
async def smt_else(message: types.Message, state: FSMContext):

    if int(message.chat.id) == int(conf.chat_id):
        return None

    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete"]
        )

    await message.delete()

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=(await message.answer(
        text="Простите, но Вы не можете писать сюда сообщения",
        reply_markup=await main_menu()
    )).message_id)
