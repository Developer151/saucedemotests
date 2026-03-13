import allure
from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = ".cart_item"
        self.item_name = ".inventory_item_name"

    @allure.step("Проверить, что товар отображается в корзине")
    def assert_item_visible(self):
        expect(self.page.locator(self.cart_item)).to_be_visible()
        allure.attach(
            self.page.screenshot(),
            name="cart_item_visible",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Проверить название товара в корзине")
    def assert_item_name(self, expected_name: str):
        expect(self.page.locator(self.item_name)).to_have_text(expected_name)
