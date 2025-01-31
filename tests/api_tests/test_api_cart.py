import pytest
import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', force=True)

BASE_URL = "https://www.sibdar-spb.ru/ajax/basketOrder.php"
HEADERS = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.sibdar-spb.ru",
    "referer": "https://www.sibdar-spb.ru/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 "
                  "YaBrowser/24.12.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
COOKIES = {
    "CONSENT": os.getenv("CONSENT", ""),
    "basketor": os.getenv("BASKETOR", ""),
    "PHPSESSID": os.getenv("PHPSESSID", ""),
    "SLO_G_WPT_TO": os.getenv("SLO_G_WPT_TO", ""),
    "SLO_GWPT_Show_Hide_tmp": os.getenv("SLO_GWPT_Show_Hide_tmp", ""),
    "SLO_wptGlobTipTmp": os.getenv("SLO_wptGlobTipTmp", "")
}


def modify_cart(item_id, action):
    payload = f"data=%7B%22idCookie%22%3A%22{COOKIES['basketor']}%22%2C%22idProd%22%3A%22{item_id}%22%2C%22type%22%3A%22{action}%22%7D"
    response = requests.post(BASE_URL, data=payload, headers=HEADERS, cookies=COOKIES)

    logging.info(f"Request: {payload}")
    logging.info(f"Response Status: {response.status_code}")
    logging.info(f"Response Headers: {response.headers}")
    logging.info(f"Response Content: {response.text}")

    return response


@pytest.mark.parametrize("item_id", [642])
def test_add_item_to_cart(item_id):
    response = modify_cart(item_id, "add")
    assert response.status_code == 200, "Ошибка добавления товара в корзину"
    assert "1" in response.text, "Некорректный ответ при добавлении товара"


@pytest.mark.parametrize("item_id", [642])
def test_increase_item_quantity(item_id):
    response = modify_cart(item_id, "plus")
    assert response.status_code == 200, "Ошибка увеличения количества товара"
    assert any(char.isdigit() and int(char) > 1 for char in response.text), "Количество товара не увеличилось"


@pytest.mark.parametrize("item_id", [642])
def test_remove_item_from_cart(item_id):
    response = modify_cart(item_id, "delete")
    assert response.status_code == 200, "Ошибка удаления товара из корзины"
    assert "0" in response.text, "Некорректный ответ при удалении товара"
