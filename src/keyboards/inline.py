from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard():
    inline_keyboard_builder = InlineKeyboardBuilder()
    inline_keyboard_builder.button(
        text='156194946',
        callback_data='156194946'
    )
    inline_keyboard_builder.button(
        text='156194947',
        callback_data='156194947'
    )
    inline_keyboard_builder.button(
        text='106744336',
        callback_data='106744336'
    )
    inline_keyboard_builder.button(
        text='145796918',
        callback_data='145796918'
    )
    inline_keyboard_builder.button(
        text='106744333',
        callback_data='106744333'
    )
    inline_keyboard_builder.button(
        text='193957902',
        callback_data='193957902'
    )
    inline_keyboard_builder.button(
        text='193957739',
        callback_data='193957739'
    )
    inline_keyboard_builder.button(
        text='193954506',
        callback_data='193954506'
    )
    inline_keyboard_builder.button(
        text='Cсылка на магазин',
        url='https://www.wildberries.ru/brands/chix'
    )

    inline_keyboard_builder.adjust(4, 4)
    return inline_keyboard_builder.as_markup()
