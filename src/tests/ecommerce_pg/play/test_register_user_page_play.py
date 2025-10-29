import random
import time

import allure
import pytest
from playwright.sync_api import Page, expect
from src.pages.ecommerce.play.home_page_play import HomePagePlay


class TestRegisterUserPlay:

    @allure.title("Test Smoke for register an account to Ecommerce page")
    @allure.description("This test verifies register account page for ecommerce.")
    @allure.tag("Register-Account", "Functional")
    @pytest.mark.functional
    @pytest.mark.smoke
    def test_register_new_user(self, page: Page, log_test_name) -> None:
        """
           Test the edit account after the user is logged
           steps:
               1. Access to Home Page
               2. Make a Hove on My account menu
               3. Register page to page
               4. Complete the required information
               5. Register the user
        """
        username = f"Juan_{random.randint(1, 100)}"
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        register_page = home_page.click_on_register_menu()
        register_page.enter_first_name(username)
        register_page.enter_last_name("Perez")
        register_page.enter_email_to_register_user(f"{username}@test.com")
        register_page.enter_phone("245341354")
        register_page.enter_password_to_register("Test123!")
        register_page.enter_confirmation_password_to_register("Test123!")
        register_page.select_private_policy()
        register_page.click_on_continue_button()
        expect(register_page.success).to_be_visible()
        expect(register_page.success).to_contain_text("Your Account Has Been Created")
        time.sleep(3)
