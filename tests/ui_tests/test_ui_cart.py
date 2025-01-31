import allure
from tests.pages.cart_page import CartPage


@allure.feature('Корзина')
@allure.story('Добавление товара в корзину')
@allure.severity(allure.severity_level.NORMAL)
def test_add_item_to_cart(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()

    with allure.step("Добавляем товар в корзину"):
        cart_page.add_item_to_cart()

    with allure.step("Проверяем, что корзина не пуста"):
        assert not cart_page.is_cart_empty(), "Корзина не должна быть пуста после добавления товара"


@allure.feature('Корзина')
@allure.story('Заполнение формы в корзине')
@allure.severity(allure.severity_level.CRITICAL)
def test_fill_in_cart_form(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()
    cart_page.add_item_to_cart()
    cart_page.open_cart()

    # Данные для заполнения формы
    name = "Иван"
    phone = "+79000000000"

    with allure.step(f"Заполняем форму: Имя - {name}, Телефон - {phone}"):
        cart_page.fill_in_cart_form(name, phone)

    with allure.step("Отправляем заказ"):
        cart_page.submit_order()

    with allure.step("Проверяем, что корзина пуста после отправки заказа"):
        assert cart_page.is_cart_empty(), "Корзина должна быть пуста после отправки заказа"


@allure.feature('Корзина')
@allure.story('Удаление товара из корзины')
@allure.severity(allure.severity_level.MINOR)
def test_remove_item_from_cart(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()
    cart_page.add_item_to_cart()
    cart_page.open_cart()

    with allure.step("Удаляем товар из корзины"):
        cart_page.remove_item_from_cart()

    with allure.step("Проверяем, что корзина пуста после удаления товара"):
        assert cart_page.is_cart_empty(), "Корзина должна быть пуста после удаления товара"
