from playwright.sync_api import Page
from playwright.sync_api import expect

class HerokuappHomePage:

    def __init__ (self, page:Page):
        self.page = page
        self.add_remove_element_link = page.get_by_role("link", name="Add/Remove Elements")

    def addRemoveLink_visible(self):
        return self.add_remove_element_link.is_visible()

    def addRemoveLinkClick(self):
        self.add_remove_element_link.click()
    
    