import pytest
import allure
from api.api_requests import CourierApiEndpoints


@allure.epic('Test Courier Creation')
class TestCourierCreation:
    api_client = CourierApiEndpoints()

    @allure.title('Создание курьера с корректными данными')
    def test_create_courier_success(self, courier_data):
        response = self.api_client.create_courier(courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Создание курьера без обязательных параметров')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_without_required_fields(self, courier_data, missing_field):
        incomplete_data = courier_data.copy()
        incomplete_data.pop(missing_field, None)

        response = self.api_client.create_courier(incomplete_data)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text

    @allure.title('Создание существующего курьера')
    def test_create_courier_duplicate(self, courier_data):
        response = self.api_client.create_courier(courier_data)
        assert response.status_code == 201

        response = self.api_client.create_courier(courier_data)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text
