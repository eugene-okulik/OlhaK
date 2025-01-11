class Endpoint:
    def __init__(self, url):
        self.url = url
        self.response = None

    def check_response_is_200(self):
        assert self.response.status_code == 200, f"Expected status 200, got {self.response.status_code}"

    def check_id_is_present(self):
        response_data = self.response.json()
        assert 'id' in response_data, "Object ID is missing"
        return response_data['id']
