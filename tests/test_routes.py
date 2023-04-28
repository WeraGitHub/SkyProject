from application import app
from application.routes import get_weather

client = app.test_client()


def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home page' in response.data


def test_about():
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Person A' in response.data
    assert b'Person B' in response.data
    assert b'Person C' in response.data


def test_get_weather():
    locations = ['Three Legged Cross', 'Isleworth', 'Chilworth']
    weather_data_list = get_weather(locations)
    assert len(weather_data_list) == len(locations)


def test_pipes():
    response = client.get('/pipes')
    assert response.status_code == 200
    assert b'CI/CD' in response.data
