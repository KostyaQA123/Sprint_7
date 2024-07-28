import allure
import pytest
import json
from api.api_requests import ScooterApiEndpoints


@allure.epic('Test Order List')
class TestOrderList:
    api_client = ScooterApiEndpoints()

    @allure.title('Получение заказов без указания параметров')
    def test_get_orders_without_parameters(self):
        response = self.api_client.get_orders()
        assert response.status_code == 200
        response_body = response.json()
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)

    @allure.title('Получение заказов для несуществующего курьера')
    def test_get_orders_with_nonexistent_courier_id(self):
        params = {'courierId': 999999999}
        response = self.api_client.get_orders(params=params)
        assert response.status_code == 404
        assert "Курьер с идентификатором" in response.text

    @allure.title('Получение заказов с пагинацией')
    @pytest.mark.parametrize("limit, page", [(10, 0), (20, 1)])
    def test_get_orders_with_pagination(self, limit, page):
        params = {'limit': limit, 'page': page}
        response = self.api_client.get_orders(params=params)
        assert response.status_code == 200
        response_body = response.json()
        assert "pageInfo" in response_body
        assert response_body["pageInfo"]["limit"] == limit
        assert response_body["pageInfo"]["page"] == page

    @allure.title('Получение заказов отфильтрованных по станциям метро')
    @pytest.mark.parametrize("nearestStation", [["1"], ["2"], ["1", "2"], ["110"]])
    def test_get_orders_filtered_by_nearest_stations(self, nearestStation):
        params = {'nearestStation': json.dumps(nearestStation)}
        response = self.api_client.get_orders(params=params)
        assert response.status_code == 200
        response_body = response.json()
        assert "orders" in response_body

        for order in response_body["orders"]:
            assert order["metroStation"] in nearestStation
