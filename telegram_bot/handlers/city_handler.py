from aiogram_dialog.widgets.input import MessageInput
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from telegram_bot.dialogs.states import Forecast

from telegram_bot.bot import dispatcher
from loguru import logger


@dispatcher.message_handler()
async def city_handler(message: Message, message_input: MessageInput, manager: DialogManager):
    manager.dialog_data.clear()
    city = message.text.strip()
    logger.info(f"City received: {city}")
    manager.dialog_data["city"] = city
    await manager.start(Forecast.MAIN, data={"city": city} , mode = StartMode.RESET_STACK)