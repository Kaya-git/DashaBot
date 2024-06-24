from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from utils import callbackdata
from keyboards.inline import main_menu
from aiogram import F
from finalstate.fsm import GarantStates
from aiogram.types import Message
from config import conf


question_router = Router(name="Вопрос")


@question_router.callback_query(callbackdata.QuestionRequest.filter(
    F.question == "question"
))
async def ask_admin(
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
    md = await query.message.answer(
        text="""
        Напишите свой вопрос. Убедитесь, что у Вас незакрытый аккаунт.
        """,
        reply_markup=await main_menu()
    )
    await state.update_data(message_to_delete=md.message_id)
    await state.set_state(GarantStates.question)


@question_router.message(GarantStates.question)
async def question_retrive(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()

    if "message_to_delete" in data:
        await conf.telegram.bot.delete_message(
            message.chat.id,
            data["message_to_delete"]
        )

    await state.update_data(question=message.text)

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=(await message.answer(
        text="""
        Благодарим Вас за обращение. Наш администратор скоро свяжется с Вами
        """,
        reply_markup=await main_menu()
    )).message_id)

    data = await state.get_data()

    await conf.telegram.bot.send_message(
        chat_id=conf.chat_id,
        text=f"""
            Новый вопрос:
            id: {data["client_telegram_id"]},
            username: {message.from_user.username}
            Message: {data["question"]}
        """
    )

    await message.delete()
