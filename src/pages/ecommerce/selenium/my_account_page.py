from selenium.webdriver.common.by import By

from src.pages.ecommerce.selenium.register_user_page import RegisterUserPage
from utils.logger import get_logger
from src.pages.ecommerce.selenium.base_page import BasePage
from config.config import BASE_URL

logger = get_logger(__name__)
class MyAccountPage(BasePage):

    register_option = (By.XPATH, "//a[text()=' Register']")

    def __init__(self, driver, environment):
        super().__init__(driver)
        url = BASE_URL[environment]
        self.url = f"{url}/index.php?route=account/login"
        self.driver.get(self.url)
        logger.info("Navigating to the page: " + self.url)

        # elements option

    def click_register_option(self):
        self.click_element(self.register_option)
        return RegisterUserPage(self.driver)

    def get_elements_option(self, element):
        return self.find_element(element)

