import requests


class DeleteObject:
    def __init__(self, url):
        self.url = url
        self.response = None

    def delete_object(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")

    def check_response_is_200(self):
        assert self.response.status_code == 200, f"Expected status 200, got {self.response.status_code}"
