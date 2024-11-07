from playwright.sync_api import Page
from elements.baidu_search_elements import BaiduSearchElements

class BaiduSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_search_term(self, term):
        self.page.fill(BaiduSearchElements.SEARCH_INPUT, term)

    def click_search(self):
        self.page.click(BaiduSearchElements.SEARCH_BUTTON)