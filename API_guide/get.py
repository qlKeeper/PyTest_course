from json.decoder import JSONDecodeError
import requests

payload = {'name': 'Pasha'}

# GET только параметры нет тела 
response = requests.get("http://playground.learnqa.ru/api/hello", params=payload)
print(response.json()['answer'])

response = requests.get("https://playground.learnqa.ru/api/get_text")

try:
    print(response.json())
except JSONDecodeError:
    print("Response is not a JSON format")