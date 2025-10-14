from playwright.sync_api import Page, Locator

from src.pages.ecommerce.play.base_page_play import BasePagePlay
from src.pages.ecommerce.play.my_account_play import MyAccountPagePlay
from src.pages.ecommerce.play.register_user_page_play import RegisterUserPlay


class HomePagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.my_account: Locator = page.get_by_role("button", name="My Account")
        self.register_menu: Locator = page.get_by_role("link", name="Register", exact=True)
        self.login_menu: Locator = page.get_by_role("link", name="Login", exact=True)

    def navigate(self):
        self.navigate_url(url="https://ecommerce-playground.lambdatest.io/")

    def hover_my_account_menu(self):
        self.hover_element(self.my_account)

    def click_on_login_menu(self):
        self.click_element(self.login_menu)
        return MyAccountPagePlay(self.page)

    def click_on_register_menu(self):
        self.click_element(self.register_menu)
        return RegisterUserPlay(self.page)