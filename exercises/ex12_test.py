import requests

def test_header_value():
    
    r = requests.get('https://playground.learnqa.ru/api/homework_header')

    assert 'Some secret value' in r.headers['x-secret-homework-header'], \
        "Значение 'x-secret-homework-header' не совпадает с ожидаемым"