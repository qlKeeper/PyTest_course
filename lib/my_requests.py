import requests
from lib.logger import Logger
import allure


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, 'POST')
    
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, 'GET')
    
    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, 'PUT')
    
    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request to URL '{url}'"):
            return MyRequests._send(url, data, headers, cookies, 'DELETE')
    
    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        
        url= f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        
        Logger.add_request(url, data, headers, cookies, method)

        match method:
            case 'GET':
                r = requests.get(url, params=data, headers=headers, cookies=cookies)
            case 'POST':
                r = requests.post(url, data=data, headers=headers, cookies=cookies)
            case 'PUT':
                r = requests.put(url, data=data, headers=headers, cookies=cookies)
            case 'DELETE':
                r = requests.delete(url, data=data, headers=headers, cookies=cookies)
            case _:
                raise Exception(f"Bad HTTP method '{method}' was received")
            

        Logger.add_response(r)
            
        return r