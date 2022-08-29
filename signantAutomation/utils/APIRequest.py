from dataclasses import dataclass
from requests.auth import HTTPBasicAuth

import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict

# Wrapper code for API's get, post and other methods and get response in more formatted and clean way.

class APIRequest:

    def get(self, url, username=None, password=None, auth=None, headers= None):
        if auth=='basic':
            basic = HTTPBasicAuth(username, password)
            response = requests.get(url, auth=basic)
        else:
            response = requests.get(url, headers=headers)
        return self.__get_responses(response)

    def post(self, url, headers, payload=None, json=None):
        response = requests.post(url, data=payload, headers=headers, json=json)
        return self.__get_responses(response)

    def put(self, url, headers, payload=None, json=None):
        response = requests.put(url, data=payload, headers=headers, json=json)
        return self.__get_responses(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )