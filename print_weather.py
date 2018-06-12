import requests

from req import get_weather

weather = get_weather('http://api.openweathermap.org/data/2.5/weather?id=524901%s&APPID=02c1c930bc0639e03991e42db1430484%s&units=metric')

print(weather)