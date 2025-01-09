import pytest
import allure

from olha_kovanova.test_api_olha_kovanova.endpoints.create_object import CreateObject
from olha_kovanova.test_api_olha_kovanova.endpoints.delete_object import DeleteObject
from olha_kovanova.test_api_olha_kovanova.endpoints.get_object import GetObject
from olha_kovanova.test_api_olha_kovanova.endpoints.update_object import UpdateObject

url = "http://167.172.172.115:52353"


@allure.story('Creating an object')
@pytest.mark.critical
def test_create_object():
    create_endpoint = CreateObject(url)
    response = create_endpoint.create_new_object("Olha's Object", "red", "medium")

    assert response.status_code == 200, "Failed to create object"
    response_data = response.json()
    object_id = response_data['id']
    print(f"New object created with ID {object_id}")
    assert object_id is not None, "Object ID should not be None"


@allure.story('Updating an object')
@pytest.mark.medium
def test_update_object(new_object):
    update_endpoint = UpdateObject(url)
    response = update_endpoint.update_object(new_object, "Olha's Updated Object", "blue", "large")

    assert response.status_code == 200, "Failed to update object"
    response_data = response.json()
    assert response_data['name'] == "Olha's Updated Object", "Object update failed"
    print("Object updated successfully")


@allure.story('Getting an object by ID')
def test_get_object_by_id(new_object):
    get_endpoint = GetObject(url)
    response = get_endpoint.get_object(new_object)

    assert response.status_code == 200, "Failed to fetch object"
    response_data = response.json()
    assert response_data['id'] == new_object, "Fetched object ID doesn't match"
    print(f"Object fetched successfully with ID {new_object}")


@allure.description('Deleting an object')
def test_delete_object(new_object):
    delete_endpoint = DeleteObject(url)
    delete_response = delete_endpoint.delete_object(new_object)

    assert delete_response.status_code == 200, f"Failed to delete object with ID {new_object}"
    print(f"Object with ID {new_object} deleted successfully")
