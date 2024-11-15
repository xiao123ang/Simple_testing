# pages/android_app_page.py
import uiautomator2 as u2
from elements.android_app_elements import AndroidAppElements

class AndroidAppPage:
    def __init__(self, device):
        self.device = device

    def enter_username(self, username):
        self.device(resourceId=AndroidAppElements.USERNAME_INPUT).set_text(username)

    def enter_password(self, password):
        self.device(resourceId=AndroidAppElements.PASSWORD_INPUT).set_text(password)

    def click_login(self):
        self.device(resourceId=AndroidAppElements.LOGIN_BUTTON).click()