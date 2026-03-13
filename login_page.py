import allure
from playwright.sync_api import Page
from config import TestData


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    @allure.step("Открыть страницу логина")
    def open(self):
        self.page.goto(TestData.BASE_URL)

    @allure.step("Авторизоваться под пользователем {username}")
    def login(self, username: str = TestData.STANDARD_USER, password: str = TestData.PASSWORD):
        self.open()
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        self.page.wait_for_selector(".inventory_list", state="visible", timeout=10000)
        allure.attach(
            self.page.screenshot(),
            name="after_login",
            attachment_type=allure.attachment_type.PNG
        )
