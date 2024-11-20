from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from telegram_bot.dialogs import states


dialog = Dialog(
    Window(
        Const("Я умею показывать погоду в разных городах, чтобы начать, введите свой город"),

        state = states.Main.MAIN,
    ),
)
