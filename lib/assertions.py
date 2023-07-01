from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_val, error_msg):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Ответ не в формате JSON. Текст ответа '{response.text}'"
            
        assert name in response_as_dict, f"Ответ JSON не имеет ключа '{name}'"
        assert response_as_dict[name] == expected_val, error_msg

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Ответ не в формате JSON. Текст ответа '{response.text}'"
            
        assert name in response_as_dict, f"Ответ JSON не имеет ключа '{name}'"
        
    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Неожиданный статус код! {response.status_code}"