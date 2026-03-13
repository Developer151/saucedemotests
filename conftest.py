import pytest
import allure
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    """
    Фикстура: создаёт страницу Playwright для каждого теста
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300,
            args=["--start-maximized"]
        )
        context = browser.new_context(viewport=None)  # полный экран
        page = context.new_page()
        
        yield page
        
        # Закрываем после теста
        context.close()
        browser.close()


@pytest.fixture
def login_page(page):
    """Фикстура для страницы логина"""
    from pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    """Фикстура для страницы каталога"""
    from pages.inventory_page import InventoryPage
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    """Фикстура для страницы корзины"""
    from pages.cart_page import CartPage
    return CartPage(page)


# Хук для Allure: скриншот при падении
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )
