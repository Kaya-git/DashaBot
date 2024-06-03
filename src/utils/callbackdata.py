from aiogram.filters.callback_data import CallbackData


class GarantInfo(CallbackData, prefix='garant'):
    garant_info: str


class MiniGame(CallbackData, prefix='minigame'):
    mini_game: str


class GarantRequest(CallbackData, prefix='request'):
    request: str


class ChixLooks(CallbackData, prefix='looks'):
    looks: str
