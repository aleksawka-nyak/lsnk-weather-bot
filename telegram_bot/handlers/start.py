from aiogram import types

from aiogram import F, Router
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode

from telegram_bot.dialogs.states import Main


router = Router()

kb = [
        [types.KeyboardButton(text="Москва")],
        [types.KeyboardButton(text="Краснодар")],
        [types.KeyboardButton(text="Санкт-Петербург")],
    ]

@router.message(F.text == "/start")
async def start(message: Message, dialog_manager: DialogManager):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb
    )
    await message.answer("Привет, " + message.from_user.first_name.capitalize(), reply_markup=keyboard)
    await dialog_manager.start(
        Main.MAIN,
        mode=StartMode.RESET_STACK,
        show_mode=ShowMode.SEND
    )
