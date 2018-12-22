from rasa_core_sdk import Action
from weather import Weather, Unit
import pyowm
owm = pyowm.OWM('eef8f2d070b797e8838d8595b3c0f164')


class ActionGetWeather(Action):
    def name(self):
        return 'action_get_weather'

    def run(self,dispatcher, tracker,domain):
        loc = ('India',tracker.get_slot('LOC'))[bool(tracker.get_slot('LOC'))]
        result = owm.weather_at_place(loc)
        result = result.get_weather()
        temp = result.get_temperature('celsius')['temp']
        dispatcher.utter_message('{} °C in {}'.format(temp,loc))
        return
'''>python -m rasa_core_sdk.endpoint --actions actions.weather'''
'''python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current --endpoints endpoints.yml'''