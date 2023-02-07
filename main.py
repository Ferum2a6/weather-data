from pyowm import OWM
from pyowm.utils.config import get_default_config

def weather():
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    
    owm = OWM("API_KEY")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place("COUNTRY CITY")
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    temp_feelslike = w.temperature('celsius')['feels_like']
    detailed_status = w.detailed_status
    humidity = w.humidity

    data = f"""
Температура: {temp}°С
Ощущается как: {temp_feelslike}°С

Влажность: {humidity}%
Статус погоды: {detailed_status}"""
    print(data)
    
weather()
