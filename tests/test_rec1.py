import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.get_by_role("textbox", name="Email or mobile number").click()
    page.get_by_role("textbox", name="Email or mobile number").fill("wrong")
    page.get_by_role("textbox", name="Email or mobile number").press("Tab")
    page.get_by_role("textbox", name="Password").fill("wrong")
    page.get_by_role("button", name="Log In").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
