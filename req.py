import requests

def get_weather(url):
	result = requests.get(url)
	if result.status_code == 200:
		return result.json()
	else:
		print('Что-то пошло не так')

if __name__ == '__main__':
	data = get_weather('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=02c1c930bc0639e03991e42db1430484')
	print(data)