import os
from datetime import datetime

from flask import render_template
from application import app
import requests

from application.person import Person

# Define global variables - this would be done if we have our API key kept as a secret and passed to us during
# execution of Jenkinsfile in the docker run command
# WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY', 'default_key')

WEATHER_API_KEY = '03cf0108f3a426eceaf55fd80047b8ef'
# In order to run and use this application you should generate your own OpenWeather API key.
# You can get a free API key by signing up here: https://openweathermap.org/


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
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + WEATHER_API_KEY
        try:
            weather_data = requests.get(url).json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            weather_data = {}
        weather_data_list.append(weather_data)
    return weather_data_list


@app.route('/pipes')
def pipes():
    title_name = "DevOps: CI/CD Tutorial"
    return render_template('pipes.html', title=title_name)
