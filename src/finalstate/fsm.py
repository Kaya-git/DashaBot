from aiogram.fsm.state import StatesGroup, State


class GarantStates(StatesGroup):
    client_telegram_id = State()
    client_cellphone_num = State()
    screen_shot = State()
    problem_text = State()
    message_to_delete = State()
    message_to_delete_2 = State()
    question = State()
    requisites = State()
