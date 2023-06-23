import requests

methods = ['GET', 'POST', 'PUT', 'DELETE']
URL = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

for method in methods:
    for param in methods:
        if method == 'GET':
            r = requests.request(method, URL, params={'method': param})
            print(method, r.text, param)
        else: 
            r = requests.request(method, URL, data={'method': param})
            print(method, r.text, param)