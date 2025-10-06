import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEcommerceHomePage:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def test_ecommerce_home_page(self):

        # navigate to the page
        self.driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

        my_account_option = self.driver.find_element(By.XPATH, "//h2[text()='New Customer']")
        print(my_account_option)
        # Click en "My account"
        # my_account_option.click()

        time.sleep(10)
        # Close the browser
        self.driver.quit()