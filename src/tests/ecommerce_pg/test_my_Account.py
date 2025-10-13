from selenium import webdriver
from selenium.webdriver.common.by import By

from src.pages.ecommerce.selenium.my_account_page import MyAccountPage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestMyAccount:

    def test_access_to_login_page(self, driver, env):
        """
        Test that my account page is loading
        """
        logger.info("Environment: %s", env)
        # create the page object
        my_account_page = MyAccountPage(driver, env)
        # verify the elements displayed
        logger.info("Verifying the Access Login page")
        new_customer_text = my_account_page.get_elements_option((By.XPATH, "//h2[text()='New Customer']")).text
        logger.info("New Customer Section: " + new_customer_text)
        assert new_customer_text == "New Customer", "New Customer section is not displayed"
        returning_customer_text = my_account_page.get_elements_option(
            (By.XPATH, "//h2[text()='Returning Customer']")).text
        logger.info("Returning Customer Section: " + returning_customer_text)
        assert returning_customer_text == "Returning Customer", "Returning Customer section is not displayed"

    def test_register_new_user(self, driver, env):
        """
         Test to verify it is possible to create a new user
        """
        first_name = (By.ID, "input-firstname")
        last_name = (By.ID, "input-lastname")
        e_mail = (By.ID, "input-email")
        phone = (By.ID, "input-telephone")
        new_password = (By.ID, "input-password")
        confirm_password = (By.ID, "input-confirm")

        logger.info("Environment: %s", env)
        # create the page object
        my_account_page = MyAccountPage(driver, env)
        register_page = my_account_page.click_register_option()
        logger.info("Verifying the User can be register")
        register_page.click_text_box_menu(first_name)
        register_page.enter_text(first_name, "Magda")
        
        new_customer_text = my_account_page.click_element((By.XPATH, "//h2[text()='New Customer']")).text
        logger.info("New Customer Section: " + new_customer_text)
        assert new_customer_text == "New Customer", "New Customer section is not displayed"
        returning_customer_text = my_account_page.get_elements_option(
            (By.XPATH, "//h2[text()='Returning Customer']")).text
        logger.info("Returning Customer Section: " + returning_customer_text)
        assert returning_customer_text == "Returning Customer", "Returning Customer section is not displayed"



