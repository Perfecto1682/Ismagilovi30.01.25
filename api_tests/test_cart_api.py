import pytest
from pages.cart_page import CartAPI


@pytest.mark.parametrize("item_id", [642])  # Пример ID товара
def test_add_item_to_cart(item_id):
    """Тест добавления товара в корзину"""
    response = CartAPI.modify_cart(item_id, "add")
    assert response.status_code == 200, "Ошибка добавления товара в корзину"
    assert response.json() == 1, "Некорректный ответ при добавлении товара"


@pytest.mark.parametrize("item_id", [642])  # Пример ID товара
def test_increase_item_quantity(item_id):
    """Тест увеличения количества товара в корзине"""
    response = CartAPI.modify_cart(item_id, "plus")
    assert response.status_code == 200, "Ошибка увеличения количества товара"
    assert response.json() > 1, "Количество товара не увеличилось"


@pytest.mark.parametrize("item_id", [642])  # Пример ID товара
def test_remove_item_from_cart(item_id):
    """Тест удаления товара из корзины"""
    response = CartAPI.modify_cart(item_id, "delete")
    assert response.status_code == 200, "Ошибка удаления товара из корзины"
    assert response.json() == 0, "Некорректный ответ при удалении товара"
