from aiogram import Bot, Router, types
from aiogram.types import CallbackQuery
from asyncio import sleep
from keyboards.inline import get_inline_keyboard


photo_dict = {
    '156194946': [
        "src/tmp/156194946/photo_2023-12-06_11-00-20.jpg",
        "src/tmp/156194946/photo_2023-12-06_11-00-21.jpg",
        "src/tmp/156194946/photo_2023-12-06_11-00-22.jpg",
        "src/tmp/156194946/photo_2023-12-06_11-00-28.jpg"
    ],
    '156194947': [
        'src/tmp/156194947/photo_2023-12-06_11-00-42.jpg',
        'src/tmp/156194947/photo_2023-12-06_11-00-49.jpg',
        'src/tmp/156194947/photo_2023-12-06_11-00-51.jpg'
    ],
    '106744336': [
        'src/tmp/106744336/photo_2023-12-06_11-01-12.jpg',
        'src/tmp/106744336/photo_2023-12-06_11-01-13.jpg',
        'src/tmp/106744336/photo_2023-12-06_11-01-15.jpg'
    ],
    '145796918': [
        'src/tmp/145796918/photo_2023-12-06_11-01-31.jpg',
        'src/tmp/145796918/photo_2023-12-06_11-01-32.jpg',
        'src/tmp/145796918/photo_2023-12-06_11-01-33.jpg'
    ],
    '106744333': [
        'src/tmp/106744333/photo_2023-12-06_11-01-46.jpg',
        'src/tmp/106744333/photo_2023-12-06_11-01-47 (2).jpg',
        'src/tmp/106744333/photo_2023-12-06_11-01-47.jpg',
        'src/tmp/106744333/photo_2023-12-06_11-01-49.jpg',
        'src/tmp/106744333/photo_2023-12-06_11-01-50.jpg'
    ],
    '193957902': [],
    '193957739': [],
    '193954506': []
}

part_number_router = Router(name="part_number")


@part_number_router.callback_query()
async def select_part_number(call: CallbackQuery, bot: Bot):
    await call.message.answer(
            text="Лови несколько удачных образов под разный повод😎",
        )
    print(call.data)
    for photo in photo_dict[call.data]:
        await call.message.answer_photo(types.FSInputFile(path=photo))
        await sleep(2)

    await call.message.answer(
        text='Хочешь больше образов? Выбирай артикул.',
        reply_markup=get_inline_keyboard()
    )
