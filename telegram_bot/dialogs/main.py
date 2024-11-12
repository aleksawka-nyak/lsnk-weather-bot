from aiogram_dialog import Dialog, Window, DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram.types import Message
from aiogram_dialog.widgets.kbd import Button, Start, Row, Back
from aiogram_dialog.widgets.text import Const
from loguru import logger
from telegram_bot.handlers import city_handler

from telegram_bot.dialogs import states
from telegram_bot.dialogs.states import Forecast


dialog = Dialog(
    Window(
        Const("Привет!"),
        Const("Я умею показывать погоду в разных городах, чтобы начать, введите свой город"),
        MessageInput(city_handler.city_handler),
        Row(
        ),
            #TODO а как реально сделать динамические кнопки (закладки)

        state = states.Main.MAIN
    )
)