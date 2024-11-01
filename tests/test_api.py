# tests/test_api.py
import pytest
import allure
from utils.request_handler import send_request

@allure.feature('User API')
@allure.story('Get User Info')
def test_get_user_info():
    url = "https://api.example.com/user/1"
    response = send_request("GET", url)
    
    with allure.step("Check response status code"):
        assert response.status_code == 200
    
    with allure.step("Check response content"):
        assert response.json().get("id") == 1