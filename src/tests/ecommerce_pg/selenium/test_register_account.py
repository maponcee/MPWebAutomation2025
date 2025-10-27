import random
from selenium.webdriver.common.by import By
from src.pages.ecommerce.selenium.my_account_page import MyAccountPage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestRegisterAccount:

    def test_register_new_user(self, driver, env, log_test_name):
        """
         Test to verify it is possible to create a new user
        """
        username = f"Juan_{random.randint(1, 100)}"
        logger.info("Environment: %s", env)
        # create the page object
        my_account_page = MyAccountPage(driver, env)
        register_page = my_account_page.click_register_option()
        logger.info("Verifying the User can be register")
        register_page.enter_first_name(username)
        register_page.enter_last_name("Perez")
        register_page.enter_email(f"{username}@test.com")
        register_page.enter_phone("5914567894")
        register_page.enter_password("Test123!")
        register_page.enter_password_confirm("Test123!")
        register_page.click_check_box_policy()
        register_page.click_continue_button()
        assert "Your Account Has Been Created!" in register_page.get_success_response().text,\
            "Account registration fails"

    def test_that_policies_are_mandatory(self, driver, env, log_test_name):
        """
         Test that policies are mandatory
        """
        username = f"Juan_{random.randint(1, 100)}"
        logger.info("Environment: %s", env)
        # create the page object
        my_account_page = MyAccountPage(driver, env)
        register_page = my_account_page.click_register_option()
        logger.info("Verifying the User can be register")
        register_page.enter_first_name(username)
        register_page.enter_last_name("Perez")
        register_page.enter_email(f"{username}@test.com")
        register_page.enter_phone("5914567894")
        register_page.enter_password("Test123!")
        register_page.enter_password_confirm("Test123!")
        register_page.click_continue_button()
        assert "You must agree to the Privacy Policy!" in register_page.get_failed_response().text, \
            "Account is register without policies"

