import requests


class DotDevApiError(Exception):
    def __init__(self, response: requests.Response):
        code = response.status_code
        text = response.text
        message = f"Unexpected Error: [{code}] {text}"
        super().__init__(message)
