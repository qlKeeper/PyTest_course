import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    # Негативный тест
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email,
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        assert response.status_code == 400, \
            f"Неожиданный статус код {response.status_code}"
        assert  response.content.decode('utf-8') == \
            f"Users with email '{email}' already exists", \
                f"Неожиданный контент ответа {response.content}"