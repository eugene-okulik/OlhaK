import requests


class DeleteObject:
    def __init__(self, base_url):
        self.base_url = base_url

    def delete_object(self, object_id):
        response = requests.delete(f"{self.base_url}/object/{object_id}")
        return response
