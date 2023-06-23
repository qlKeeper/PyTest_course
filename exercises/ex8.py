import requests, time

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

token, seconds_wait = requests.get(URL).json().values()
status = requests.get(URL, params={'token': token}).json().keys()

if status == 'error':
    print('Error status')
    exit()
else:
    time.sleep(seconds_wait)

r = requests.get(URL, params={'token': token}).json()

print('result' in r and 'status' in r)
