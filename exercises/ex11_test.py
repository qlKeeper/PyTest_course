import requests

def test_cookie_value():

    r = requests.get('https://playground.learnqa.ru/api/homework_cookie')

    assert 'Max-Age=2678400' in r.headers.get('Set-Cookie'), \
        'Значение куки не совпадает'