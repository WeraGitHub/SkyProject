from flask import render_template
from application import app
import requests


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    title_name = "Home page"
    return render_template('home.html', title=title_name)


@app.route('/about')
def about():
    return render_template('about.html', title="About us and our project")


@app.route('/weather', methods=["GET"])
def weather_w():
    weather_data = get_weather(['Three Legged Cross', 'Romford', 'Limassol'])
    return render_template('weather.html', title="Weather App", weather_data=weather_data)


def get_weather(locations):
    weather_data_list = []
    for location in locations:
        weather_api_key = '03cf0108f3a426eceaf55fd80047b8ef'
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + weather_api_key
        try:
            weather_data = requests.get(url).json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            weather_data = {}
        weather_data_list.append(weather_data)
    return weather_data_list
