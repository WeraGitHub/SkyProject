from datetime import datetime

from flask import render_template
from application import app
import requests

from application.person import Person


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    title_name = "Home page"
    return render_template('home.html', title=title_name)


@app.route('/about')
def about():
    person_a = Person('Person A', 'Surname-A', datetime(1981, 1, 10), "blue")
    person_b = Person('Person B', 'Surname-B', datetime(1991, 2, 11), "green")
    person_c = Person('Person C', 'Surname-C', datetime(1989, 3, 12), "yellow")
    people = [person_a, person_b, person_c]
    return render_template('about.html', title="About this project", people=people)


@app.route('/weather', methods=["GET"])
def weather():
    weather_data = get_weather(['Three Legged Cross', 'Isleworth', 'Chilworth'])
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
