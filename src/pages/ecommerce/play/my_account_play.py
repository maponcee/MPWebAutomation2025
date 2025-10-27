from playwright.sync_api import Page, Locator
from src.pages.ecommerce.play.base_page_play import BasePagePlay
from src.pages.ecommerce.play.register_user_page_play import RegisterUserPlay


class MyAccountPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.register: Locator = page.get_by_role("link", name=" Register")
        self.email: Locator = page.get_by_role("textbox", name="E-Mail Address")
        self.password: Locator = page.get_by_role("textbox", name="Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.my_account: Locator = page.get_by_role("heading", name="My Account")
        self.edit_your_account: Locator = page.get_by_role("link", name=" Edit your account")
        self.register: Locator = page.get_by_role("link", name=" Register")
        self.success_my_account: Locator = page.get_by_text("Success: Your account has")

    def click_on_register_link(self):
        self.click_element(self.register)
        return RegisterUserPlay(self.page)

    def click_on_email_field(self):
        self.click_element(self.email)

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def click_on_password_field(self):
        self.click_element(self.password)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def click_on_login_button(self):
        self.click_element(self.login_button)

    def login_to_account(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_login_button()

    def click_on_edit_your_account(self):
        self.click_element(self.edit_your_account)
        return EditAccountPlay(self.page)

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
