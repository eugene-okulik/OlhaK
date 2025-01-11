import pytest
from olha_kovanova.test_api_olha_kovanova.endpoints.create_object import CreateObject

BASE_URL = "http://167.172.172.115:52353/object"


@pytest.fixture
def new_object():
    create_endpoint = CreateObject(BASE_URL)
    create_endpoint.create_new_object("Olha's Object", "red", "medium")
    create_endpoint.check_response_is_200()
    return create_endpoint.check_id_is_present()
