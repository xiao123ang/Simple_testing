# tests/test_baidu_search.py
import pytest
import allure
from pages.baidu_search_page import BaiduSearchPage

@allure.feature('UI Tests')
@allure.story('Baidu Search Test')
def test_baidu_search(browser):
    page = browser.new_page()
    page.goto("https://www.baidu.com")

    search_page = BaiduSearchPage(page)
    search_page.enter_search_term("Playwright")
    search_page.click_search()

    # Verify that results are displayed
    page.wait_for_selector("#content_left")
    assert "Playwright" in page.title()

    page.close()