import requests
import json
import allure


url = "http://167.172.172.115:52353/object"


@allure.story('Get an object')
def all_posts():
    response = requests.get(url)
    if response.status_code == 200:
        print("All posts/objects:", response.json())
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")


all_posts()


# Delete created object
@allure.story('Delete an object')
def clear(object_id):
    response = requests.delete(f'{url}/{object_id}')
    if response.status_code == 200:
        print("Object was deleted successfully!")
    else:
        print(f"Error updating object! Status code: {response.status_code}")
        print("Response from server:", response.text)


# create an object
@allure.story('Creating multiple objects')
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

    if response.status_code == 200:
        print("New object was added successfully!")
        response_data = response.json()  # Get the response data
        print("Response from server:", response_data)
        return response.json()['id']  # Return the 'id' of the newly created object
    else:
        print("Error during post a new object!")
        print("Error code:", response.status_code)
        print("Error text:", response.text)


# Update an existing object (PUT request)
@allure.story('Updating an object')
def put_a_object():
    object_id = new_object()  # First create the object and get its ID
    body = {
        "name": "Olha's 2nd Object",
        "data": {
            "color": "green",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}

    # Make the PUT request to update the object
    response = requests.put(f"{url}/{object_id}", json=body, headers=headers)

    if response.status_code == 200:
        print("Object updated successfully with method PUT!")
        response_data = response.json()  # Parse the response JSON
        print("Updated object response:", response_data)
        assert response_data['name'] == "Olha's 2nd Object"  # Verify the update
    elif response.status_code == 204:
        print("Object updated successfully with no content returned.")
    else:
        print(f"Error updating object! Status code: {response.status_code}")
        print("Response from server:", response.text)
    clear(object_id)


put_a_object()


# Update an existing object (PATCH request)
@allure.story('Updating an object')
def patch_a_object():
    object_id = new_object()  # First create the object and get its ID
    body = {
        "name": "Olha's 3nd Object",
        "data": {
            "color": "ping"
        }
    }
    headers = {'Content-Type': 'application/json'}

    # Make the PATCH request to update the object
    response = requests.patch(f"{url}/{object_id}", json=body, headers=headers)

    if response.status_code == 200:
        print("Object updated successfully with method PATCH!")
        response_data = response.json()  # Parse the response JSON
        print("Updated object response:", response_data)
        assert response_data['name'] == "Olha's 3nd Object"  # Verify the update
    elif response.status_code == 204:
        print("Object updated successfully with no content returned.")
    else:
        print(f"Error updating object! Status code: {response.status_code}")
        print("Response from server:", response.text)
    clear(object_id)


patch_a_object()
