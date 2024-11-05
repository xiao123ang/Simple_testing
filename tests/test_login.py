# tests/test_login.py
import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@allure.feature('UI Tests')
@allure.story('Login Test')
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com/login")

        login_page = LoginPage(page)
        login_page.enter_username("testuser")
        login_page.enter_password("password")
        login_page.click_login()

        # Add assertions to verify successful login
        assert "Dashboard" in page.title()

        browser.close()