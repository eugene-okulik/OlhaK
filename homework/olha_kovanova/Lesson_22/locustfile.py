import locust
from locust import task, HttpUser


class NewObject(HttpUser):
    host = "http://167.172.172.115:52353/object"
    wait_time = locust.constant(1)

    @task
    def get_object(self):
        self.client.get('host', headers={'Content-Type': 'application/json'})
