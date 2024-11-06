# pages/baidu_search_page.py
from playwright.sync_api import Page

class BaiduSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = "input[name='wd']"
        self.search_button = "input[type='submit']"

    def enter_search_term(self, term):
        self.page.fill(self.search_input, term)

    def click_search(self):
        self.page.click(self.search_button)