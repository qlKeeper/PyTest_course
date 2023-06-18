import requests

headers = {'some_header': '123'}

r = requests.get("http://playground.learnqa.ru/api/show_all_headers", headers=headers)
print(r.text)
print(r.headers)