import requests
import allure
import json


class CourierApiEndpoints:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    def create_courier(self, data):
        with allure.step(f"POST {self.BASE_URL}/api/v1/courier"):
            response = requests.post(f"{self.BASE_URL}/api/v1/courier", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def login_courier(self, data):
        with allure.step(f"POST {self.BASE_URL}/api/v1/courier/login"):
            response = requests.post(f"{self.BASE_URL}/api/v1/courier/login", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def delete_courier(self, courier_id):
        with allure.step(f"DELETE {self.BASE_URL}/api/v1/courier/{courier_id}"):
            response = requests.delete(f"{self.BASE_URL}/api/v1/courier/{courier_id}")
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response


class ScooterApiEndpoints:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    def create_order(self, data):
        with allure.step(f"POST {self.BASE_URL}/api/v1/orders"):
            response = requests.post(f"{self.BASE_URL}/api/v1/orders", json=data)
            allure.attach(json.dumps(data), name="body", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response

    def get_orders(self, params=None):
        with allure.step(f"GET {self.BASE_URL}/api/v1/orders"):
            response = requests.get(f"{self.BASE_URL}/api/v1/orders", params=params)
            allure.attach(json.dumps(params), name="params", attachment_type=allure.attachment_type.JSON)
            allure.attach(response.text, name="response", attachment_type=allure.attachment_type.JSON)
            return response
