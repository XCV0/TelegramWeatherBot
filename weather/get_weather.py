from pyowm import OWM
import asyncio
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


# Default settings
mgr = None
config_dict = get_default_config()
config_dict['language'] = 'ru'


async def on_startup():
    global mgr
    owm = OWM('your free OWM API key', config_dict)
    mgr = owm.weather_manager()


async def get_weather(city):
    global mgr
    observation = mgr.weather_at_place('London,GB')
    w = observation.weather

    return w
# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())