from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='156194946'),
            KeyboardButton(text='156194947'),
            KeyboardButton(text='106744336'),
            KeyboardButton(text='145796918'),

        ],
        [
            KeyboardButton(text='106744333'),
            KeyboardButton(text='193957902'),
            KeyboardButton(text='193957739'),
            KeyboardButton(text='193954506'),
        ]
    ],
    resize_keyboard=True
)


cancel_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)
