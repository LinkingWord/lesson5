from datetime import datetime

from flask import Flask, abort, request

from news_list import all_news
from req import get_weather

city_id = 524901
apikey = '02c1c930bc0639e03991e42db1430484'

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric' (city_id, apikey)
    weather = get_weather(url)
    cur_date = datetime.now().strftime('%d.%m.%Y')
    
    result = '<p><b>Температура:</b> %s\n</p>' % weather['main']['temp']
    result += '<p><b>Город:</b> %s</p>' % weather['name']
    result += '<p><b>Дата:</b> %s</p>' % cur_date
    return result

@app.route('/news')
def all_the_news():
    colors = ['green', 'red', 'blue', 'magenta']
    try:
        limit = int(request.args.get('limit'))
    except:
        limit = 10
    color = request.args.get('color', 'black') if request.args.get('color') in colors else 'black'
    # for item in request.args:
    #     print(item)
    #     print(request.args.get(item))
    return '<h1 style="color: %s">News: <small>%s</small><h/1>' % (color, limit)

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news ['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)