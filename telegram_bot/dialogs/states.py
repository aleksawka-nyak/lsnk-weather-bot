from aiogram.fsm.state import State, StatesGroup


class Main(StatesGroup):
    MAIN = State()


class Forecast(StatesGroup):
    MAIN = State()
