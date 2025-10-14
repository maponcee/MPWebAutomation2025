import re
from playwright.sync_api import Page, expect

from src.pages.ecommerce.play.home_page_play import HomePagePlay
from src.pages.ecommerce.play.my_account_play import MyAccountPagePlay


class TestMyAccountPlay:
    def test_login(self, page: Page) -> None:
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        my_account_page = home_page.click_on_login_menu()
        my_account_page.enter_email("bnmponce@gmail.com")
        my_account_page.enter_password("Test123!")
        my_account_page.click_on_login_button()

    def test_edit_account_information(self, page: Page) -> None:
        my_account_page = MyAccountPagePlay(page)
        my_account_page.navigate()
        my_account_page.login_to_account("bnmponce@gmail.com", "Test123!")
        my_account_page.click_on_edit_your_account()
        my_account_page.enter_first_name("MagdaUpdate")
        my_account_page.enter_last_name("Test Last Name")
        my_account_page.click_on_continue_button()
