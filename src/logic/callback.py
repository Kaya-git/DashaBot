# from aiogram import Router, types
# from aiogram.fsm.context import FSMContext
# from aiogram.types import CallbackQuery
# from asyncio import sleep
# from keyboards.inline import get_inline_keyboards
# from utils import callbackdata
# from aiogram import F
# from finalstate.fsm import GarantStates
# from aiogram.types import Message


# logic_router = Router(name="logic_router")

# @logic_router.callback_query()
# async def select_part_number(call: CallbackQuery):
#     await call.message.answer(
#             text="Лови несколько удачных образов под разный повод😎",
#         )
#     print(call.data)
#     for photo in photo_dict[call.data]:
#         img_path = types.FSInputFile(photo)
#         print(img_path)
#         await call.message.answer_photo(photo=img_path)
#         await sleep(2)

#     await call.message.answer(
#         text='Хочешь больше образов? Выбирай артикул.',
#         reply_markup=get_inline_keyboard()
#     )
