from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import callbackdata


async def get_main_inline_keyboard():
    inline_keyboard_builder = InlineKeyboardBuilder()

    inline_keyboard_builder.button(
        text='Гарантия 6 месяцев',
        callback_data=callbackdata.GarantRequest(
            request='garant_request'
        )
    )

    # inline_keyboard_builder.button(
    #     text='Мини-игра',
    #     callback_data=callbackdata.MiniGame(
    #         mini_game='mini_game'
    #     )
    # )

    inline_keyboard_builder.button(
        text='Обращение по гарантии',
        callback_data=callbackdata.GarantInfo(
            garant_info='garant'
        )
    )

    inline_keyboard_builder.button(
        text='Задать вопрос',
        callback_data=callbackdata.QuestionRequest(
            question='question'
        )
    )

    inline_keyboard_builder.adjust(1, 1, 1, 1)
    return inline_keyboard_builder.as_markup()


async def main_menu():
    inline_keyboard_builder = InlineKeyboardBuilder()

    inline_keyboard_builder.button(
        text="главное меню",
        callback_data=callbackdata.MenuRequest(
            menu="menu"
        )
    )
    return inline_keyboard_builder.as_markup()
