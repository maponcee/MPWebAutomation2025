import re
import time

from playwright.sync_api import Page, expect

from src.pages.ecommerce.play.home_page_play import HomePagePlay


class TestEditAccountPlay:
    def test_edit_account_information(self, page: Page) -> None:
        """
        Test the edit account after the user is logged
        steps:
           1. Access to Home Page
           2. access to the Login page
           3. Login to page
           4. Update the first and Last name
        """
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        my_account_page.login_to_account("bnmponce@gmail.com", "Test123!")
        edit_account_page = my_account_page.click_on_edit_your_account()
        edit_account_page.enter_first_name("MagdaUpdate")
        edit_account_page.enter_last_name("Test Last Name")
        edit_account_page.click_on_continue_button()
        expect(my_account_page.success_my_account).to_be_visible()
        expect(my_account_page.success_my_account).to_contain_text("Your account has been successfully updated.")
        time.sleep(3)


