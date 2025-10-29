import time

import allure
import pytest
from playwright.sync_api import Page, expect

from src.pages.ecommerce.play.home_page_play import HomePagePlay
from utils.logger import get_logger

logger = get_logger(__name__)


class TestMyAccountPlay:
    @allure.title("Test Smoke for Login Ecommerce page")
    @allure.description("This test verifies login page for ecommerce.")
    @allure.tag("Account", "Functional")
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_login(self, page: Page, log_test_name) -> None:
        """
        Test the login process with existing user.
        steps:
           1. Access to Home Page
           2. Make a hove on My account menu
           3. Click on Login button
           4. Enter the valid credentials
           5. Click on Login page
        """
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        my_account_page.enter_email("bnmponce@gmail.com")
        my_account_page.enter_password("Test123!")
        my_account_page.click_on_login_button()
        expect(my_account_page.edit_your_account).to_be_visible()
        time.sleep(3)

    @allure.title("Test Smoke for Failed Login Ecommerce page")
    @allure.description("This test verifies failed login page for ecommerce.")
    @allure.tag("Account", "Functional")
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, message_error, scenario", [
        ("test5", "clave123", "Warning: No match for E-Mail Address and/or Password.",
         "Username and Password is not register in the data base"),
        ("", "Test123!", "Warning: No match for E-Mail Address and/or Password.", "empty user name"),
        ("bnmponce@gmail.com", "", "Warning: No match for E-Mail Address and/or Password.", "Empty password"),
        ("test02@test.com", "=1' or '1=1'", "Warning: No match for E-Mail Address and/or Password.", "sql injection"),
        ("bnmponce@gmail.com", "Password123!", "Warning: No match for E-Mail Address and/or Password.",
         "Password doesn't belong to register user"),
    ],
    )
    def test_failed_loging(self, page: Page, username, password, message_error, scenario, log_test_name):
        """
        This test case is to verify that it is not possible to complete the login when the provided credentials
        are invalid.
        """
        logger.info(f"Test scenario:{scenario} with username:{username} password: {password}")
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        my_account_page.enter_email(username)
        my_account_page.enter_password(password)
        my_account_page.click_on_login_button()
        response = my_account_page.get_failed_message()
        assert message_error == response, f"Expected response: {message_error}, Actual Result: {response}"
