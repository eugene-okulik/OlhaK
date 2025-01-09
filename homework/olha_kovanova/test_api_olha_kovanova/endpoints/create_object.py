import requests


class CreateObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_new_object(self, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.base_url}/object", json=body, headers=headers)
        return response
