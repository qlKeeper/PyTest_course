import requests

payload = {
    'login': 'secret_login',
    'password': 'secret_pass',
    }

r = requests.get('http://playground.learnqa.ru/api/get_auth_cookie', params=payload)

cookies = {}
if r.cookies.get('auth_cookie') is not None:
    cookies = {'auth_cookie': r.cookies.get('auth_cookie')}

r = requests.get("https://playground.learnqa.ru/api/check_auth_cookie", \
                 cookies=cookies)
print(r.text)