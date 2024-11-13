from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager, ShowMode
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Start, Row, Back
from aiogram_dialog.widgets.text import Const, Format
from loguru import logger

from telegram_bot.dialogs import states
from telegram_bot.parser import forecast_parser

async def add_favourite(callback: CallbackQuery, button: Button, manager: DialogManager):
    city = manager.start_data["city"]
    logger.info(f"{city} is added to favourites")
    await callback.message.answer("added")

async def get_forecast(dialog_manager: DialogManager, **kwargs):
    city = dialog_manager.start_data["city"]
    logger.info(f"city in getter is {city}")
    if not city:
        logger.warning("City not found in dialog_data. Please check city_handler.")
        return {"forecast": "Не удалось получить данные о погоде."}
    logger.info(f"Fetching weather for city in get_forecast: {city}")
    weather = 'lsnk-weather-bot ' + forecast_parser(city)

    markdown_weather = f"```{weather}```"

    return {
        "forecast": markdown_weather
    }

dialog = Dialog(
    Window(
        Format("{forecast}"),
        Button(
            Const("В избранное"),
            id="favourite",
            on_click=add_favourite
        ),
        state=states.Forecast.MAIN,
        getter=get_forecast
    )
)