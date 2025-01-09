import pytest
from endpoints.create_object import CreateObject
from olha_kovanova.test_api_olha_kovanova.endpoints.delete_object import DeleteObject

url = "http://167.172.172.115:52353"


@pytest.fixture(scope='function')
def new_object():
    create_endpoint = CreateObject(url)
    response = create_endpoint.create_new_object("Olha's Object", "red", "medium")
    assert response.status_code == 200, "Failed to create object"
    response_data = response.json()
    object_id = response_data['id']
    yield object_id  # this will be used in the tests
    # Cleanup after the test
    delete_endpoint = DeleteObject(url)
    delete_endpoint.delete_object(object_id)
