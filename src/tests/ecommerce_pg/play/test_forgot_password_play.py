import allure
import pytest
from config.config import user_name
from playwright.sync_api import Page, expect
from src.pages.ecommerce.play.home_page_play import HomePagePlay
from utils.logger import get_logger

logger = get_logger(__name__)


class TestForgotPasswordPlay:

    @allure.title("Test Smoke for Forgot Password page")
    @allure.description("This test verifies forgot Password page for ecommerce.")
    @allure.tag("Account", "Functional")
    @pytest.mark.functional
    def test_forgot_password(self, page: Page, log_test_name) -> None:
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        forgot_password_page = my_account_page.click_on_forgot_password()
        forgot_password_page.enter_email_for_forgot_password(user_name)
        forgot_password_page.click_on_continue_button()
        expect(my_account_page.reset_confirmation).to_be_visible()
        expect(my_account_page.reset_confirmation).to_contain_text(
            "An email with a confirmation link has been sent your email address.")

    @allure.title("Test Smoke for Forgot Password page")
    @allure.description("This test verifies forgot Password page for ecommerce.")
    @allure.tag("Account", "Functional")
    @pytest.mark.functional
    @pytest.mark.parametrize("email, message_error, scenario", [
        ("test5", "Warning: The E-Mail Address was not found in our records, please try again!",
         "Value sent is not an email"),
        ("", "Warning: The E-Mail Address was not found in our records, please try again!", "empty email"),
        ("test012654564@test.com.io", "Warning: The E-Mail Address was not found in our records, please try again!",
         "Email sent is not register"),
    ],)
    def test_email_is_validated(self, page: Page, email, message_error, scenario, log_test_name) -> None:
        """
        This test is to verify that emails is validated in forgot password
        """
        logger.info(f"Test scenario:{scenario}")
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        forgot_password_page = my_account_page.click_on_forgot_password()
        forgot_password_page.enter_email_for_forgot_password(email)
        forgot_password_page.click_on_continue_button()
        response = forgot_password_page.get_fp_failed_message()
        assert message_error == response, f"Expected response: {message_error}, Actual Result: {response}"
