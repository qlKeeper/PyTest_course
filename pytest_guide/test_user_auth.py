# Позитивный тест

import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234',
        }

        r1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)
        
        assert 'auth_sid' in r1.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in r1.headers, "There is no CSRF token header in respon"
        assert "user_id" in r1.json(), "There is no user id in the response"

        auth_sid = r1.cookies.get("auth_sid")
        token = r1.headers.get('x-csrf-token')
        user_id_from_auth_method = r1.json()['user_id']

        r2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={'x-csrf-token': token},
            cookies={'auth_sid': auth_sid},
        )

        assert 'user_id' in r2.json(), "There is no user id in the second response"

        user_id_from_check_method = r2.json()['user_id']

        assert user_id_from_auth_method == user_id_from_check_method, \
        "User id from auth method is not equal to user id from check method"
