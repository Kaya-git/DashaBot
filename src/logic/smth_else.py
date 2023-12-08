from aiogram import Router, types


smth_else_router = Router(name="smth_else")


@smth_else_router.message()
async def smt_else(message: types.Message):
    await message.delete()
    await message.answer(
        text="Прости, но ты не можешь писать сюда сообщения",
    )
