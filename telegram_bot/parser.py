import requests
from loguru import logger


def forecast_parser(city: str):
    """Получает информацию о погоде для заданного города."""
    logger.info(f"Fetching weather for city: {city}")
    url = f'https://wttr.in/{city}?T&m&0&lang=ru'  # Форматируем URL для запроса
    response = requests.get(url)

    if response.status_code == 200:
        data = str(response.text)
        if data:
            # # Разделяем строку на отдельные значения
            # weather_info = data[0].split()
            # # Присваиваем значения переменным
            # description = weather_info[0]  # Описание погоды
            # temperature = weather_info[1]   # Температура
            # humidity = weather_info[2]       # Влажность
            # wind = weather_info[3]           # Скорость ветра
            # pressure = weather_info[4]       # Давление
            #
            # # Возвращаем информацию о погоде в виде словаря
            # dict = {
            #     "description": description,
            #     "temperature": temperature,
            #     "humidity": humidity,
            #     "wind": wind,
            #     "pressure": pressure
            # }
            return (data)

        else:
            return ValueError("Не удалось получить данные о погоде.")
    else:
        return ValueError("Не удалось получить данные о погоде. Проверьте название города.")
