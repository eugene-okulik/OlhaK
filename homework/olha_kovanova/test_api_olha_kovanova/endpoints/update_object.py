import requests


class UpdateObject:

    def __init__(self, base_url):
        self.base_url = base_url

    def update_object(self, object_id, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f"{self.base_url}/object/{object_id}", json=body, headers=headers)
        return response
