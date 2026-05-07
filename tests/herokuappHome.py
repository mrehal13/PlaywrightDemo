from playwright.sync_api import sync_playwright
from pages.herokuapp_home import HerokuappHomePage
from playwright.sync_api import Page

def test_link(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    add_remove_link_test = HerokuappHomePage(page)
    add_remove_link_test.addRemoveLink_visible()
    add_remove_link_test.addRemoveLinkClick()
    print("!!!!!!! PAGE TITLE IS ========= " + page.title())

