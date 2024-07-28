import pytest

from api.api_requests import CourierApiEndpoints
from utils.data_generator import generate_random_string


@pytest.fixture
def courier_data():
    return {
       "login": generate_random_string(),
       "password": generate_random_string(),
       "firstName": generate_random_string()
    }


@pytest.fixture
def courier():
    api_client = CourierApiEndpoints()
    courier_data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    create_response = api_client.create_courier(courier_data)
    assert create_response.status_code == 201
    assert "ok" in create_response.json()

    login_data = {
        "login": courier_data["login"],
        "password": courier_data["password"]
    }
    login_response = api_client.login_courier(login_data)
    assert login_response.status_code == 200
    courier_id = login_response.json()["id"]

    yield courier_data

    delete_response = api_client.delete_courier(courier_id)
    assert delete_response.status_code == 200
    assert delete_response.json()["ok"]


@pytest.fixture
def order_data():
    return {
        "firstName": generate_random_string(),
        "lastName": generate_random_string(),
        "address": generate_random_string(),
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "No comment",
    }
