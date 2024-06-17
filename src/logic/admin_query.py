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


question_router = Router(name="Вопрос")


@question_router.callback_query(callbackdata.QuestionRequest.filter(
    F.question == "question"
))
async def ask_admin(
    query: CallbackQuery,
    state: FSMContext
):

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.message_to_delete)

    await state.update_data(message_to_delete=await query.message.answer(
        text="""
        Напиши свой вопрос. Убедись, что у тебя незакрытый аккаунт.
        """,
        reply_markup=await main_menu()
    ))
    await state.set_state(GarantStates.question)


@question_router.message(GarantStates.question)
async def question_retrive(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()
    await data["message_to_delete"].delete()

    await state.update_data(question=message.text)

    await state.set_state(GarantStates.message_to_delete)
    await state.update_data(message_to_delete=await message.answer(
        text="""
        Благодарим вас за обращение. Наш администратор скоро свяжется с вами
        """,
        reply_markup=await main_menu()
    ))

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
