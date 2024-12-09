import pytest
import requests
import json

url = "http://167.172.172.115:52353/object"


# Define fixture for setup and teardown of the tests
@pytest.fixture(scope='session', autouse=True)
def start_and_finish_testing():
    print("Start testing")
    yield
    print("Testing completed")


# Define fixture to run before and after every test
@pytest.fixture(scope='function', autouse=True)
def before_and_after_test():
    print("before test")
    yield
    print("after test")


# Define fixture for creating an object before each test and deleting it afterward
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


# Test case for creating multiple objects with different data using pytest.mark.parametrize
@pytest.mark.critical
@pytest.mark.parametrize("name, color, size", [
    ("Olha's Object 1", "red", "medium"),
    ("Olha's Object 2", "blue", "large"),
    ("Olha's Object 3", "green", "small")
])
def test_create_object(name, color, size, new_object):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=body, headers=headers)

    assert response.status_code == 200, f"Failed to create object {name}"
    response_data = response.json()
    object_id = response_data['id']
    print(f"New object '{name}' was added successfully with ID {object_id}")


# Test case for updating an object using PUT request
@pytest.mark.medium
def test_put_a_object(new_object):
    object_id = new_object  # Use the ID from the fixture
    body = {
        "name": "Olha's 2nd Object",
        "data": {
            "color": "green",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{url}/{object_id}", json=body, headers=headers)

    assert response.status_code == 200, "Failed to update object"
    response_data = response.json()
    assert response_data['name'] == "Olha's 2nd Object", "Object update failed"
    print("Object updated successfully with PUT!")


# Test case for updating an object using PATCH request
def test_patch_a_object(new_object):
    object_id = new_object  # Use the ID from the fixture
    body = {
        "name": "Olha's 3rd Object",
        "data": {
            "color": "pink"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"{url}/{object_id}", json=body, headers=headers)

    assert response.status_code == 200, "Failed to update object"
    response_data = response.json()
    assert response_data['name'] == "Olha's 3rd Object", "Object update failed"
    print("Object updated successfully with PATCH!")


# Test case for getting an object by ID
def test_get_object_by_id(new_object):
    object_id = new_object  # Use the ID from the fixture
    response = requests.get(f"{url}/{object_id}")

    assert response.status_code == 200, "Failed to fetch object"
    response_data = response.json()
    assert response_data['id'] == object_id, "Fetched object ID doesn't match"
    print("Object fetched successfully by ID!")


# Test case for deleting an object and verifying its deletion
def test_delete_object(new_object):
    object_id = new_object  # Use the ID from the fixture

    # Verify that the object no longer exists by sending a GET request
    response = requests.get(f"{url}/{object_id}")

    # Ensure that the object is no longer available
    assert response.status_code == 200, f"Object with ID {object_id} was not deleted. GET request returned \
                                        {response.status_code}"
    print(f"Object with ID {object_id} is successfully deleted and not found anymore.")
