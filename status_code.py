import requests

# 500 code, error server
response = requests.post("http://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)


# 404 code, error client
response = requests.post("http://playground.learnqa.ru/api/some")
print(response.status_code)
print(response.text)

# 301, 302 code redirecting
r = requests.post("http://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = r.history[0]
second_response = r

print(first_response.url)
print(second_response.url)