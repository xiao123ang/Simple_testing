# tests/test_baidu_search.py
import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.baidu_search_page import BaiduSearchPage

@allure.feature('UI Tests')
@allure.story('Baidu Search Test')
def test_baidu_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.baidu.com")

        search_page = BaiduSearchPage(page)
        search_page.enter_search_term("Playwright")
        search_page.click_search()

        # Verify that results are displayed
        page.wait_for_selector("#content_left")
        assert "Playwright" in page.title()

        browser.close()