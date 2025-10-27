from selenium.webdriver.common.by import By
from src.pages.ecommerce.selenium.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class RegisterUserPage(BasePage):
    # locators
    private_policy = (By.ID, "input-agree")
    continue_button = (By.CLASS_NAME, "btn.btn-primary")
    first_name = (By.ID, "input-firstname")
    last_name = (By.ID, "input-lastname")
    e_mail = (By.ID, "input-email")
    phone = (By.ID, "input-telephone")
    new_password = (By.ID, "input-password")
    confirm_password = (By.ID, "input-confirm")
    success = (By.CLASS_NAME, "page-title.my-3")
    registration_failed = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")


    def click_text_box_menu(self, text_box):
        self.click_element(text_box)

    def get_text_box_menu_item(self, text_box):
        return self.find_element(text_box)

    def enter_first_name(self, name):
        self.enter_text(self.first_name, name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_email(self, email):
        self.enter_text(self.e_mail, email)

    def enter_phone(self, phone):
        self.enter_text(self.phone, phone)

    def enter_password(self, password):
        self.enter_text(self.new_password, password)

    def enter_password_confirm(self, password):
        self.enter_text(self.confirm_password, password)

    def click_continue_button(self):
        self.scroll_to_element(self.continue_button)
        self.click_element(self.continue_button)

    def get_check_box_policy(self):
        return self.find_element(self.private_policy)

    def click_check_box_policy(self):
        self.scroll_to_element(self.private_policy)
        policy_checkbox = self.find_element(self.private_policy)
        if not policy_checkbox.is_selected():
            policy_checkbox.click()

    def get_success_response(self):
        return self.find_element(self.success)

    def get_failed_response(self):
        return  self.find_element(self.registration_failed)
