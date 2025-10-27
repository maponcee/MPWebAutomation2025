import random
from selenium.webdriver.common.by import By
from src.pages.ecommerce.selenium.my_account_page import MyAccountPage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestMyAccount:

    def test_access_to_login_page(self, driver, env, log_test_name):
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

