from playwright.sync_api import sync_playwright
from pages.herokuapp_checkboxes import HerokuappCheckboxPage
from playwright.sync_api import Page

def test_link(page:Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox_test = HerokuappCheckboxPage(page)
    checkbox_test.checkbox1_visible()
    checkbox_test.checkbox2_visible()
    checkbox_test.checkbox1_click()
    checkbox_test.checkbox2_click()

    print("!!!!!!! PAGE TITLE IS ========= " + page.title())

