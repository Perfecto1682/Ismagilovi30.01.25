from pages.cart_page import CartPage


def test_add_item_to_cart(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()
    cart_page.add_item_to_cart()
    assert not cart_page.is_cart_empty(), "Корзина не должна быть пуста после добавления товара"


def test_fill_in_cart_form(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()
    cart_page.add_item_to_cart()
    cart_page.open_cart()

    # Данные для заполнения формы
    name = "Иван"
    phone = "+79000000000"

    cart_page.fill_in_cart_form(name, phone)
    cart_page.submit_order()

    # Проверим, что после отправки заказа корзина пуста
    assert cart_page.is_cart_empty(), "Корзина должна быть пуста после отправки заказа"


def test_remove_item_from_cart(browser):
    cart_page = CartPage(browser)
    cart_page.open()
    cart_page.select_category()
    cart_page.add_item_to_cart()
    cart_page.open_cart()

    # Удаление товара из корзины
    cart_page.remove_item_from_cart()

    # Проверим, что корзина пуста после удаления
    assert cart_page.is_cart_empty(), "Корзина должна быть пуста после удаления товара"
