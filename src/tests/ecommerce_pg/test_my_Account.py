import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from src.pages.ecommerce.my_account_page import MyAccountPage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestMyAccount:
    @classmethod
    def setup_class(self):
        # start the session
        self.driver = webdriver.Chrome()
        logger.info("Starting the session")
        self.driver.implicitly_wait(10)

    def test_access_to_login_page(self):
        """
        Test that my account page is loading
        """
        new_customer_option = (By.XPATH, "//h2[text()='New Customer']")
        # create the page object
        my_account_page = MyAccountPage(self.driver)
        # verify the elements displayed
        logger.info("Verifying the Access Login page")
        new_customer_text = my_account_page.get_elements_option((By.XPATH, "//h2[text()='New Customer']")).text
        logger.info("New Customer Section: " + new_customer_text)
        assert new_customer_text == "New Customer", "New Customer section is not displayed"
        returning_customer_text = my_account_page.get_elements_option(
            (By.XPATH, "//h2[text()='Returning Customer']")).text
        logger.info("Returning Customer Section: " + returning_customer_text)
        assert returning_customer_text == "Returning Customer", "Returning Customer section is not displayed"

    @classmethod
    def teardown_class(self):
        # Close the browser
        logger.info("Closing the browser")
        self.driver.quit()
