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


garant6months_router = Router(name="Гарантия на 6 месяцев")

MESSAGE: str = None


@garant6months_router.callback_query(callbackdata.GarantRequest.filter(
    F.request == "garant_request"
))
async def garantrequest(
    query: CallbackQuery,
    state: FSMContext
):
    await conf.prev_reply.delete()
    await state.set_state(GarantStates.client_telegram_id)
    await state.update_data(client_telegram_id=query.from_user.id)

    await state.set_state(GarantStates.client_cellphone_num)

    conf.prev_reply = await query.message.answer(
        text="для получения продвинутой гарантии, напишите, пожалуйста, ваше имя и номер телефона "
    )


@garant6months_router.message(GarantStates.client_cellphone_num)
async def cellphonerequest(
    message: Message,
    state: FSMContext
):
    await conf.prev_reply.delete()

    await state.update_data(client_cellphone_num=message.text)

    conf.prev_reply = await message.reply(
        text="""
        Поздравляем!
        Теперь при возникновении любой проблемы в течение 6 месяцев
        вы можете связаться с нами через этот бот
        (по кнопке «Обращение по гарантии»),
        и наш менеджер поможет вам с решением проблемы!
        """,
        reply_markup=get_inline_keyboards.get_main_inline_keyboard()
    )

    data = await state.get_data()

    await conf.telegram.bot.send_message(
        378288967,
        f"""
            Новая гарантия:
            id: {data["client_telegram_id"]},
            Message: {data["client_cellphone_num"]}
        """
    )
    await state.clear()
    await sleep(5)
    await message.delete()
