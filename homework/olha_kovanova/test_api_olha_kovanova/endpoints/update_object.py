from olha_kovanova.test_api_olha_kovanova.endpoints.endpoint import Endpoint
import requests


class UpdateObject(Endpoint):
    def __init__(self, url):
        super().__init__(url)

    def update_object_with_put(self, object_id, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        headers = {'Content-Type': 'application/json'}
        self.response = requests.put(f"{self.url}/{object_id}", json=body, headers=headers)

    def update_object_with_patch(self, object_id, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        headers = {'Content-Type': 'application/json'}
        self.response = requests.patch(f"{self.url}/{object_id}", json=body, headers=headers)
