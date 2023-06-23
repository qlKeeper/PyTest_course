import requests

r = requests.get("https://playground.learnqa.ru/api/long_redirect")

print(len(r.history))
print(r.url)
