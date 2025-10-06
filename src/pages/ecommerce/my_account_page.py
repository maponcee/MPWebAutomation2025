from selenium.webdriver.common.by import By

from utils.logger import get_logger
from src.pages.ecommerce.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

logger = get_logger(__name__)
class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

        # elements option

    def click_elements_option(self, element):
        return self.click_element(element)

    def get_elements_option(self, element):
        return self.find_element(element)

