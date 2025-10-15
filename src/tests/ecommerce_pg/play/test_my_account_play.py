import re
import time

from playwright.sync_api import Page, expect

from src.pages.ecommerce.play.home_page_play import HomePagePlay


class TestMyAccountPlay:
    def test_login(self, page: Page) -> None:
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

