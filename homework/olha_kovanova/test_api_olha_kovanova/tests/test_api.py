import pytest
import allure
from olha_kovanova.test_api_olha_kovanova.endpoints.create_object import CreateObject
from olha_kovanova.test_api_olha_kovanova.endpoints.delete_object import DeleteObject
from olha_kovanova.test_api_olha_kovanova.endpoints.get_object import GetObject
from olha_kovanova.test_api_olha_kovanova.endpoints.update_object import UpdateObject


BASE_URL = "http://167.172.172.115:52353/object"


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


@allure.story('Creating multiple objects')
@pytest.mark.critical
@pytest.mark.parametrize("name, color, size", [
    ("Olha's Object 1", "red", "medium"),
    ("Olha's Object 2", "blue", "large"),
    ("Olha's Object 3", "green", "small")
])
def test_create_object(name, color, size, new_object):
    create_endpoint = CreateObject(BASE_URL)
    create_endpoint.create_new_object(name, color, size)
    create_endpoint.check_response_is_200()
    object_id = create_endpoint.check_id_is_present()
    print(f"New object '{name}' was added successfully with ID {object_id}")


@allure.story('Updating an object with put')
@pytest.mark.medium
def test_put_a_object(new_object):
    update_endpoint = UpdateObject(BASE_URL)
    update_endpoint.update_object_with_put(new_object, "Olha's 2nd Object", "green", "medium")
    update_endpoint.check_response_is_200()
    print("Object updated successfully with PUT!")


@allure.story('Updating an object with patch')
def test_patch_a_object(new_object):
    update_endpoint = UpdateObject(BASE_URL)
    update_endpoint.update_object_with_patch(new_object, "Olha's 3rd Object", "pink", "medium")
    update_endpoint.check_response_is_200()
    print("Object updated successfully with PATCH!")


@allure.story('Get an object')
def test_get_object_by_id(new_object):
    get_endpoint = GetObject(BASE_URL)
    get_endpoint.get_object(new_object)
    get_endpoint.check_response_is_200()
    print("Object fetched successfully by ID!")


@allure.description('Check that object has deleted')
def test_delete_object(new_object):
    delete_endpoint = DeleteObject(BASE_URL)
    delete_endpoint.delete_object(new_object)
    delete_endpoint.check_response_is_200()
    print(f"Object with ID {new_object} is successfully deleted and not found anymore.")
