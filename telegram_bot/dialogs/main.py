from aiogram_dialog import Dialog, Window, DialogManager, ShowMode, StartMode
from aiogram_dialog.widgets.text import Const

from telegram_bot.dialogs import states


dialog = Dialog(
    Window(
        Const("Привет!"),
        Const("Я умею показывать погоду в разных городах, чтобы начать, введите свой город"),
            #TODO а как реально сделать динамические кнопки (закладки)
        state = states.Main.MAIN,
    ),
)