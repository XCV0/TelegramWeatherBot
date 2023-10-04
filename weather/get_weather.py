from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config


# Default settings
mgr = None
config_dict = get_default_config()
config_dict['language'] = 'ru'


def on_startup():
    global mgr
    owm = OWM('4b6cb6e603d0f3d7a0b930e16be556d6', config_dict)
    mgr = owm.weather_manager()


def get_weather(city):
    try:
        global mgr
        observation = mgr.weather_at_place(city)
        w = observation.weather

        return w

    except NotFoundError:
        return False


def more_weather(city):
    forecast = mgr.weather_at_place(city, 'daily')
    answer = forecast.will_be_clear_at(timestamps.tomorrow())


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