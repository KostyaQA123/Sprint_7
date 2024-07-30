import requests
import allure
import json
from api.api_configs import BASE_URL, ENDPOINTS


class CourierApiEndpoints:
    BASE_URL = BASE_URL

    def create_courier(self, data):
        endpoint = ENDPOINTS['create_courier']
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def login_courier(self, data):
        endpoint = ENDPOINTS['login_courier']
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def delete_courier(self, courier_id):
        endpoint = ENDPOINTS['delete_courier']
        with allure.step(f"DELETE {self.BASE_URL}{endpoint}{courier_id}"):
            response = requests.delete(f"{self.BASE_URL}{endpoint}{courier_id}")
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response


class ScooterApiEndpoints:
    BASE_URL = BASE_URL

    def create_order(self, data):
        endpoint = ENDPOINTS['create_order']
        with allure.step(f"POST {self.BASE_URL}{endpoint}"):
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def get_orders(self, params=None):
        endpoint = ENDPOINTS['get_orders']
        with allure.step(f"GET {self.BASE_URL}{endpoint}"):
            response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
            allure.attach(json.dumps(params), name="params", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response
