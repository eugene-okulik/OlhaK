import pytest
import requests

url = "http://167.172.172.115:52353/object"


@pytest.fixture
def new_object():
    body = {
        "name": "Olha's Object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=body, headers=headers)
    assert response.status_code == 200, "Failed to create object"
    response_data = response.json()
    object_id = response_data['id']
    print(f"New object created with ID {object_id}")
    return object_id
