import numpy as np
from locust import task
from locust import between
from locust import HttpUser

sample = {
  "seniority": 3,
  "home": "owner",
  "time": 36,
  "age": 26,
  "marital": "single",
  "records": "no",
  "job": "freelance",
  "expenses": 35,
  "income": 0.0,
  "assets": 60000.0,
  "debt": 3000.0,
  "amount": 800,
  "price": 1000
}

class CreditRiskTestUser(HttpUser):
    
    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)