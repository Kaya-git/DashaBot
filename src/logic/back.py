from aiogram import F, Router, types
from keyboards import kb_main_menu

back_router = Router(name="back")


@back_router.message(F.text == 'Назад')
async def cancel(message: types.Message):
    await message.answer(
        text='Назад',
        reply_markup=kb_main_menu
    )
    await message.delete()
