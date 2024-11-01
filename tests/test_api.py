# tests/test_api.py
import pytest
import allure
from utils.request_handler import send_request, send_websocket_message_sync

@allure.feature('User API')
@allure.story('Get User Info')
@pytest.mark.parametrize("user_id, expected_status, expected_id", [
    (1, 200, 1),
    (2, 200, 2),
    (3, 404, None),
])
def test_get_user_info(user_id, expected_status, expected_id):
    url = f"https://api.example.com/user/{user_id}"
    response = send_request("GET", url)
    
    with allure.step("Check response status code"):
        assert response.status_code == expected_status
    
    with allure.step("Check response content"):
        if expected_id is not None:
            assert response.json().get("id") == expected_id
        else:
            assert response.json().get("id") is None

@allure.feature('WebSocket API')
@allure.story('Send and Receive Message')
def test_websocket_message():
    uri = "wss://example.com/socket"
    message = "Hello, WebSocket!"
    
    with allure.step("Send and receive WebSocket message"):
        response = send_websocket_message_sync(uri, message)
        assert response == "Expected response"