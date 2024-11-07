# 用py封装方法的定位
from playwright.sync_api import Page
from elements.baidu_search_elements import BaiduSearchElements

class BaiduSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_search_term(self, term):
        self.page.fill(BaiduSearchElements.SEARCH_INPUT, term)

    def click_search(self):
        self.page.click(BaiduSearchElements.SEARCH_BUTTON)


#用ini存放元素，再调用
from playwright.sync_api import Page
from utils.config_reader import read_locator

class BaiduSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def enter_search_term(self, term):
        search_input = read_locator('baidu_search_page', 'search_input')
        self.page.locator(search_input).fill(term)

    def click_search(self):
        search_button = read_locator('baidu_search_page', 'search_button')
        self.page.locator(search_button).click()