# tests/test_api.py
import pytest
import allure
from utils.request_handler import send_request
from utils.data_loader import load_csv_data, load_json_data, load_excel_data

@allure.feature('User API')
@allure.story('Get User Info')
@pytest.mark.parametrize("user_id, expected_status, expected_id", load_csv_data('data/test_data.csv'))
def test_get_user_info_csv(user_id, expected_status, expected_id):
    url = f"https://api.example.com/user/{user_id}"
    response = send_request("GET", url)
    
    with allure.step("Check response status code"):
        assert response.status_code == expected_status
    
    with allure.step("Check response content"):
        if expected_id is not None:
            assert response.json().get("id") == expected_id
        else:
            assert response.json().get("id") is None

# You can similarly use load_json_data or load_excel_data for other tests