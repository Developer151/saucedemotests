# 🧪 SauceDemo AutoTests

Автоматизированные тесты для интернет-магазина [SauceDemo](https://www.saucedemo.com/) с использованием **Playwright + Pytest + Allure**.
# Структура проекта:
saucedemo_tests/
├── pages/ # Page Objects

│ ├── login_page.py # Страница логина

│ ├── inventory_page.py # Страница каталога

│ └── cart_page.py # Страница корзины

├── test_cart.py # Тесты корзины

├── conftest.py # Фикстуры Playwright

├── config.py # Тестовые данные

├── requirements.txt # Зависимости

└── README.md # Инструкция

## 🛠 Технологии

- **Python 3.10+**
- **Playwright** — управление браузером
- **Pytest** — запуск тестов
- **Allure** — отчёты
- **Page Object Model** — архитектура

## ⚙️ Установка

### 1. Клонировать репозиторий
```
git clone <url-репозитория>
```
```
cd saucedemo_tests
```
### 2. Установить зависимости
```
pip install -r requirements.txt
```
### 3. Установить браузер
```
playwright install chromium
```
**Без отчёта**
```
pytest test_cart.py -v
```
**С Allure отчётом, одна команда на запуск тестов, генерацию и вывод отчёта**
```
pytest test_cart.py -v --alluredir=allure-results && allure serve allure-results
```
Что тестируется

1.Позитивный сценарий

2.Авторизация под standard_user

3.Добавление случайного товара в корзину

4.Проверка, что тоdар появился в корзине

Покрытие:
- ✅ Логин

- ✅ Добавление товара

- ✅ Переход в корзину

- ✅ Проверка наличия товара
