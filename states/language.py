from aiogram.dispatcher.filters.state import StatesGroup, State


class get_lang(StatesGroup):
    lang = State()