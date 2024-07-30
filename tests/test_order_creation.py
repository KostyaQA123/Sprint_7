import allure
import pytest
from api.api_requests import ScooterApiEndpoints


@allure.epic('Test Order Creation')
class TestOrderCreation:
    api_client = ScooterApiEndpoints()

    @allure.title('Создание заказа')
    def test_create_order_contains_track(self, order_data):
        response = self.api_client.create_order(order_data)
        assert response.status_code == 201
        response_body = response.json()
        assert "track" in response_body and type(response_body["track"]) is int

    @allure.title('Создание заказа с различными цветами самоката')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order_with_various_colors(self, order_data, color):
        order_data['color'] = color
        response = self.api_client.create_order(order_data)
        assert response.status_code == 201
        assert "track" in response.json()
