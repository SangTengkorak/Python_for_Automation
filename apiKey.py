import requests as rq

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'

parameters = {'APPID': '[APIKEY VALUE]',
              'q': 'Seattle,US'}

response = rq.get(baseUrl, params=parameters)

print(response.content)
