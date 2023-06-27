from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_val, error_msg):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, \
                f"Response is not in JSON format. Response text is '{response.text}'"
            
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_val, error_msg