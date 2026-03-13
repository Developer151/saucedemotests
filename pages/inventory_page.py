import random
import allure
from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_buttons_selector = "button[data-test^='add-to-cart']"
        self.cart_link = ".shopping_cart_link"
        self.cart_badge = ".shopping_cart_badge"

    @allure.step("Добавить случайный товар в корзину")
    def add_random_item_to_cart(self):
        buttons = self.page.locator(self.add_buttons_selector).all()
        assert buttons, "Нет доступных товаров для добавления"
        
        # Запоминаем название товара (для отчёта)
        item_container = random.choice(buttons).locator("xpath=ancestor::div[@class='inventory_item']")
        item_name = item_container.locator(".inventory_item_name").text_content()
        
        allure.attach(f"Выбран товар: {item_name}", name="selected_item", attachment_type=allure.attachment_type.TEXT)
        
        random.choice(buttons).click()
        
        # Проверяем, что счётчик обновился
        expect(self.page.locator(self.cart_badge)).to_be_visible()
        allure.attach(
            self.page.screenshot(),
            name="after_add_to_cart",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.page.click(self.cart_link)
        allure.attach(
            self.page.screenshot(),
            name="cart_page",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> str:
        badge = self.page.locator(self.cart_badge)
        if badge.is_visible():
            return badge.text_content()
        return "0"
