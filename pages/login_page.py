# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#login"

    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)