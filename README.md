# weather_nlu
A bot which answers weather related questions

# Usage
python -m rasa_core_sdk.endpoint --actions actions.weather #Action server

python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/current --endpoints endpoints.yml #Chatbot