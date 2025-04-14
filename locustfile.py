# locustfile.py

from locust import HttpUser, task, between
import random

class InferenceUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict(self):
        # Generate normalized 28x28 image data with values from 0-1
        image_data = [[random.uniform(0, 1) for _ in range(28)] for _ in range(28)]

        self.client.post(
            "/predict",
            json={"data": image_data}
        )
