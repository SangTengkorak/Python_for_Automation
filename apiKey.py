import requests as rq

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'

parameters = {'APPID': '095455229389d93586d11625eeee668d',
              'q': 'Seattle,US'}

response = rq.get(baseUrl, params=parameters)

print(response.content)
