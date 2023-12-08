from aiogram import Router, types
from aiogram.types import CallbackQuery
from asyncio import sleep
from keyboards.inline import get_inline_keyboard


photo_dict = {
    '156194946': [
        "tmp/156194946/photo_2023-12-06_11-00-20.jpg",
        "tmp/156194946/photo_2023-12-06_11-00-21.jpg",
        "tmp/156194946/photo_2023-12-06_11-00-22.jpg",
        "tmp/156194946/photo_2023-12-06_11-00-28.jpg"
    ],
    '156194947': [
        'tmp/156194947/photo_2023-12-06_11-00-42.jpg',
        'tmp/156194947/photo_2023-12-06_11-00-49.jpg',
        'tmp/156194947/photo_2023-12-06_11-00-51.jpg'
    ],
    '106744336': [
        'tmp/106744336/photo_2023-12-06_11-01-12.jpg',
        'tmp/106744336/photo_2023-12-06_11-01-13.jpg',
        'tmp/106744336/photo_2023-12-06_11-01-15.jpg'
    ],
    '145796918': [
        'tmp/145796918/photo_2023-12-06_11-01-31.jpg',
        'tmp/145796918/photo_2023-12-06_11-01-32.jpg',
        'tmp/145796918/photo_2023-12-06_11-01-33.jpg'
    ],
    '106744333': [
        'tmp/106744333/photo_2023-12-06_11-01-46.jpg',
        'tmp/106744333/photo_2023-12-06_11-01-47 (2).jpg',
        'tmp/106744333/photo_2023-12-06_11-01-47.jpg',
        'tmp/106744333/photo_2023-12-06_11-01-49.jpg',
        'tmp/106744333/photo_2023-12-06_11-01-50.jpg'
    ],
    '193957902': [],
    '193957739': [],
    '193954506': []
}

part_number_router = Router(name="part_number")


@part_number_router.callback_query()
async def select_part_number(call: CallbackQuery):
    await call.message.answer(
            text="Лови несколько удачных образов под разный повод😎",
        )
    print(call.data)
    for photo in photo_dict[call.data]:
        img_path = types.FSInputFile(photo)
        print(img_path)
        await call.message.answer_photo(photo=img_path)
        await sleep(2)

    await call.message.answer(
        text='Хочешь больше образов? Выбирай артикул.',
        reply_markup=get_inline_keyboard()
    )
