from playwright.sync_api import Page, Locator
from src.pages.ecommerce.play.base_page_play import BasePagePlay


class EditAccountPlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.first_name: Locator = page.get_by_role("textbox", name="First Name *")
        self.last_name: Locator = page.get_by_role("textbox", name="Last Name*")
        self.continue_button = page.get_by_role("button", name="Continue")

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.first_name, last_name)

    def click_on_continue_button(self):
        self.click_element(self.continue_button)

