import requests


class GetObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_object(self, object_id):
        response = requests.get(f"{self.base_url}/object/{object_id}")
        return response
