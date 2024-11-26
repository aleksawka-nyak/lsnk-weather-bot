import aiohttp
from loguru import logger


async def forecast_parser(city: str) -> str:
    """Получает информацию о погоде для заданного города.
    :param city: Название города
    :returns: Информация о погоде в виде строки
    """
    logger.info(f"Fetching weather for city: {city}")
    url = f'https://wttr.in/{city}?T&m&M&0&lang=ru'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
