# tests/test_android_app.py
import pytest
import allure
import uiautomator2 as u2
from pages.android_app_page import AndroidAppPage

@allure.feature('Mobile UI Tests')
@allure.story('Android App Login Test')
def test_android_login():
    # Connect to the device
    device = u2.connect()  # Connect to the first available device

    # Launch the app
    device.app_start("com.example.android")

    app_page = AndroidAppPage(device)
    app_page.enter_username("testuser")
    app_page.enter_password("password")
    app_page.click_login()

    # Add assertions to verify successful login
    # Example: assert device(text="Welcome").exists

    device.app_stop("com.example.android")