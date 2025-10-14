from playwright.sync_api import Page, Locator
from src.pages.ecommerce.play.base_page_play import BasePagePlay


class RegisterUserPlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators
        self.first_name: Locator = page.get_by_role("textbox", name="First Name*")
        self.last_name: Locator = page.get_by_role("textbox", name="Last Name*")
        self.e_mail: Locator = page.get_by_role("textbox", name="E-Mail*")
        self.phone: Locator = page.get_by_role("textbox", name="Telephone*")
        self.register_password: Locator = page.get_by_role("textbox", name="Password*")
        self.register_conf_pass: Locator = page.get_by_role("textbox", name="Password Confirm*")
        self.private_policies: Locator = page.get_by_text("I have read and agree to the")
        self.continue_button: Locator = page.get_by_role("button", name="Continue")
        self.success: Locator = page.get_by_role("heading", name=" Your Account Has Been")

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_email_to_register_user(self, email):
        self.enter_text(self.e_mail, email)

    def enter_phone(self, phone):
        self.enter_text(self.phone, phone)

    def enter_password_to_register(self, password):
        self.enter_text(self.register_password, password)

    def enter_confirmation_password_to_register(self, password):
        self.enter_text(self.register_conf_pass, password)

    def select_private_policy(self):
        self.click_element(self.private_policies)

    def click_on_continue_button(self):
        self.click_element(self.continue_button)

