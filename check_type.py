import requests

URL = "https://playground.learnqa.ru/api"

response = requests.get(f"{URL}/check_type", params={'param1': 'value1'})
print(response.text)

response = requests.post(f"{URL}/check_type", data={'param2': 'value2'})
print(response.text)
