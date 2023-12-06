from aiogram import Router, types
from aiogram import F
from keyboards import cancel_button
from asyncio import sleep


part_number_router = Router(name="part_number")
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


@part_number_router.message(F.text == '156194946')
async def part_num_1(message: types.Message):
    await message.delete()
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["156194946"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)


@part_number_router.message(F.text == '156194947')
async def part_num_2(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["156194947"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '106744336')
async def part_num_3(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["106744336"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '145796918')
async def part_num_4(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["145796918"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '106744333')
async def part_num_5(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["106744333"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '193957902')
async def part_num_6(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["193957902"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '193957739')
async def part_num_7(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["193957739"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()


@part_number_router.message(F.text == '193954506')
async def part_num_8(message: types.Message):
    await message.answer(
        text="Лови несколько удачных образов под разный повод😎",
        reply_markup=cancel_button
    )
    await sleep(1)
    for photo in photo_dict["193954506"]:
        await message.answer_photo(
            photo=types.FSInputFile(
                path=photo
            )
        )
        await sleep(2)
    await message.delete()
