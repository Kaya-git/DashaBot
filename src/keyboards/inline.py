from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import callbackdata


class InKeyboards:
    inline_keyboard_builder = InlineKeyboardBuilder()

    def get_inline_keyboard(self):

        self.inline_keyboard_builder.button(
            text='156194946',
            callback_data='156194946'
        )
        self.inline_keyboard_builder.button(
            text='156194947',
            callback_data='156194947'
        )
        self.inline_keyboard_builder.button(
            text='106744336',
            callback_data='106744336'
        )
        self.inline_keyboard_builder.button(
            text='145796918',
            callback_data='145796918'
        )
        self.inline_keyboard_builder.button(
            text='106744333',
            callback_data='106744333'
        )
        self.inline_keyboard_builder.button(
            text='193957902',
            callback_data='193957902'
        )
        self.inline_keyboard_builder.button(
            text='193957739',
            callback_data='193957739'
        )
        self.inline_keyboard_builder.button(
            text='193954506',
            callback_data='193954506'
        )
        self.inline_keyboard_builder.button(
            text='Cсылка на магазин',
            url='https://www.wildberries.ru/brands/chix'
        )

        self.inline_keyboard_builder.adjust(4, 4)
        return self.inline_keyboard_builder.as_markup()

    def get_main_inline_keyboard(self):

        self.inline_keyboard_builder.button(
            text='Мини-игра',
            callback_data=callbackdata.MiniGame(
                mini_game='mini_game'
            )
        )

        self.inline_keyboard_builder.button(
            text='Гарантия 6 месяцев',
            callback_data=callbackdata.GarantRequest(
                request='garant_request'
            )
        )

        self.inline_keyboard_builder.button(
            text='Обращение по гарантии',
            callback_data=callbackdata.GarantInfo(
                garant_info='garant'
            )
        )

        self.inline_keyboard_builder.button(
            text='Посмотреть образы',
            callback_data=callbackdata.GarantInfo(
                garant_info='looks'
            )
        )
        self.inline_keyboard_builder.adjust(1, 1, 1, 1)
        return self.inline_keyboard_builder.as_markup()


get_inline_keyboards = InKeyboards()
