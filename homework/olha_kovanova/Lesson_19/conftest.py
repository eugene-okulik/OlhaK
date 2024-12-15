import pytest
import requests

url = "http://167.172.172.115:52353/object"


@pytest.fixture
def new_object():
    # Create a new object and return its ID
    body = {
        "name": "Olha's Object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 200, "Failed to create new object"
    response_data = response.json()
    object_id = response_data['id']
    print(f"Created new object with ID: {object_id}")

    # Return the ID of the created object
    yield object_id

    # Cleanup after test: delete the created object
    delete_response = requests.delete(f'{url}/{object_id}')
    assert delete_response.status_code == 200, "Failed to delete the object"
    print(f"Deleted object with ID: {object_id}")
