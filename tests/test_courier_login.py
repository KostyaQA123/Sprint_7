import allure
import pytest
from api.api_requests import CourierApiEndpoints
from utils.expected_data import EXP_DATA


@allure.epic('Test Courier Login')
class TestCourierLogin:
    api_client = CourierApiEndpoints()

    @allure.title('Логин курьера с корректными данными')
    def test_courier_login_success(self, courier):
        login_response = self.api_client.login_courier(courier)
        assert login_response.status_code == 200
        assert "id" in login_response.json()

    @allure.title('Логин курьера без обязательных параметров')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_without_required_fields(self, courier, missing_field):
        incomplete_data = courier.copy()
        incomplete_data[missing_field] = ""

        response = self.api_client.login_courier(incomplete_data)
        assert response.status_code == 400
        assert EXP_DATA['missing_login_data'] in response.text

    @allure.title('Логин курьера с некорректным паролем')
    def test_courier_login_with_incorrect_password(self, courier):
        wrong_password_data = courier.copy()
        wrong_password_data["password"] += "qa"

        response = self.api_client.login_courier(wrong_password_data)
        assert response.status_code == 404
        assert EXP_DATA['account_not_found'] in response.text

    @allure.title('Логин несуществующего курьера')
    def test_courier_login_nonexistent_courier(self):
        nonexistent_courier_data = {
            "login": "maybe_this_login_not_exists",
            "password": "maybe_this_password_not_exists"
        }

        response = self.api_client.login_courier(nonexistent_courier_data)
        assert response.status_code == 404
        assert EXP_DATA['account_not_found'] in response.text
