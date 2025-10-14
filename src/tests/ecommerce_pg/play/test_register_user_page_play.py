import re
from playwright.sync_api import Page, expect
from src.pages.ecommerce.play.home_page_play import HomePagePlay


class TestRegisterUserPlay:

    def test_register_new_user(self, page: Page) -> None:
        home_page = HomePagePlay(page)
        home_page.navigate()
        home_page.hover_my_account_menu()
        register_page = home_page.click_on_register_menu()
        register_page.enter_first_name("Juan")
        register_page.enter_last_name("Perez")
        register_page.enter_email_to_register_user("juan_perex@test.com")
        register_page.enter_phone("245341354")
        register_page.enter_password_to_register("Test123!")
        register_page.enter_confirmation_password_to_register("Test123!")
        register_page.select_private_policy()
        register_page.click_on_continue_button()
        expect(register_page.success).to_be_visible()
        expect(register_page.success).to_contain_text("Your Account Has Been Created")

