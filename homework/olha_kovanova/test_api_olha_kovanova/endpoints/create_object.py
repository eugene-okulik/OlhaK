import requests
from olha_kovanova.test_api_olha_kovanova.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    def __init__(self, url):
        super().__init__(url)

    def create_new_object(self, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(self.url, json=body, headers=headers)
