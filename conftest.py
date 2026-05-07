import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser1():
    with sync_playwright() as p:
        browser2 = p.chromium.launch(headless=False)
        yield browser2
        browser2.close()

@pytest.fixture()
def page1(browser1):
    page1 = browser1.new_page()
    yield page1
    page1.close()
