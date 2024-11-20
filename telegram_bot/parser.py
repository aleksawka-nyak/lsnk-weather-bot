import requests
from loguru import logger


async def forecast_parser(city: str) -> str:
    """Получает информацию о погоде для заданного города.
    :param city: Название города
    """

    logger.info(f"Fetching weather for city: {city}")
    url = f'https://wttr.in/{city}?T&m&M&0&lang=ru'
    response = requests.get(url)

    if response.status_code == 200:
        data = str(response.text)

        if data:
            return data

        else:
            return "Не удалось получить данные о погоде."
    else:
        return "Не удалось получить данные о погоде. Проверьте название города."
