from selenium.webdriver.common.by import By

from src.pages.ecommerce.selenium.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class RegisterUserPage(BasePage):
    # locators
    private_policy = (By.ID, "input-agree")
    continue_button = (By.CLASS_NAME, "btn.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)

    def click_text_box_menu(self, text_box):
        self.click_element(text_box)

    def get_text_box_menu_item(self, text_box):
        return self.find_element(text_box)

    def enter_value_in_text_(self, text_box, user_name):
        self.enter_text(text_box, user_name)

    def click_continue_button(self):
        self.scroll_to_element(self.continue_button)
        self.click_element(self.continue_button)

    def get_check_box_policy(self):
        return self.find_element(self.private_policy)

    def click_check_box_policy(self):
        self.click_element(self.private_policy)
