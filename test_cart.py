import allure
from config import TestData


@allure.feature("Корзина")
@allure.story("Добавление товаров")
class TestCart:

    @allure.title("Добавление случайного товара в корзину")
    @allure.description("Авторизация, добавление случайного товара, проверка корзины")
    def test_add_random_item_to_cart(self, login_page, inventory_page, cart_page):
        # 1. Авторизация
        login_page.login()

        # 2. Добавление случайного товара
        inventory_page.add_random_item_to_cart()

        # 3. Переход в корзину
        inventory_page.go_to_cart()

        # 4. Проверка корзины
        cart_page.assert_item_visible()
