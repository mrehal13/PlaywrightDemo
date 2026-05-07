from playwright.sync_api import Page
from playwright.sync_api import expect

class HerokuappCheckboxPage:

    def __init__ (self, page:Page):
        self.page = page
        #self.checkbox1 = page.get_by_role("checkbox", name=" checkbox 1")

        self.checkbox1 = page.locator("//*[@id='checkboxes']/input[1]")
       
        self.checkbox2 = page.locator("//*[@id='checkboxes']/input[2]")

    def checkbox1_visible(self):
        return self.checkbox1.is_visible()
    
    def checkbox1_click(self):
        self.checkbox1.check()

        

    def checkbox2_visible(self):
        return self.checkbox2.is_visible()
    
    def checkbox2_click(self):
        self.checkbox2.check()
    
    