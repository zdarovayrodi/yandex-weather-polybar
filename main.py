import requests

# send request to yandex weather api
TOKEN = 'your token'
LAT = 'your latitude'
LON = 'your longitude'
LANG = 'ru_RU'  # see in docs 

# example of request from docs
# https://yandex.ru/dev/weather/doc/dg/concepts/forecast-info.html
'''
GET https://api.weather.yandex.ru/v2/informers?
 lat=<широта>
 & lon=<долгота>
 & [lang=<язык ответа>]

X-Yandex-API-Key: <значение ключа>
'''

# response
try:
    response = requests.get('https://api.weather.yandex.ru/v2/informers?lat={}&lon={}&lang={}'.format(LAT, LON, LANG),
        headers={'X-Yandex-API-Key': TOKEN}).json()
        
    # print what you want to see
    TEMP_REAL = response['fact']['temp']
    TEMP_FEEL = response['fact']['feels_like']
        
    # in condition i dont want - and _ symbols
    CONDITION = response['fact']['condition'].replace('-', ' ').replace('_', ' ')

    # output
    print(TEMP_REAL, TEMP_FEEL, CONDITION)
except:
    exit()

