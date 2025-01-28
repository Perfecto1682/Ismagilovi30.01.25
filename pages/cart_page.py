import logging
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import requests


class CartPage:
    """Класс для работы с корзиной"""

    URL = "https://www.sibdar-spb.ru/"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """Открыть главную страницу"""
        try:
            logging.info(f"Открытие страницы: {self.URL}")
            self.browser.get(self.URL)
            WebDriverWait(self.browser, 40).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except TimeoutException as e:
            logging.error(f"Не удалось открыть страницу {self.URL}: {e}")
            raise

    def select_category(self):
        """Выбрать категорию, чтобы увидеть товары"""
        try:
            logging.info("Попытка выбрать категорию")
            category_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='bx_1847241719_15']"))
            )
            category_button.click()
            logging.info("Категория успешно выбрана")
        except TimeoutException as e:
            logging.error(f"Не удалось выбрать категорию: {e}")
            raise

    def add_item_to_cart(self):
        """Добавить товар в корзину"""
        try:
            logging.info("Попытка добавить товар в корзину")
            add_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[attr_item*='50']"))
            )
            add_button.click()
            logging.info("Товар успешно добавлен в корзину")
        except TimeoutException as e:
            logging.error(f"Не удалось добавить товар в корзину: {e}")
            raise

    def open_cart(self):
        """Открыть корзину для заполнения формы"""
        try:
            logging.info("Попытка открыть корзину")
            cart_icon = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='bask_btn'] div[class$='icon']"))
            )
            cart_icon.click()
            logging.info("Корзина успешно открыта")
        except TimeoutException as e:
            logging.error(f"Не удалось открыть корзину: {e}")
            raise

    def fill_in_cart_form(self, name, phone):
        """Заполнить форму в корзине"""
        try:
            logging.info("Заполнение формы в корзине")

            # Заполнение полей формы
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class*='name']"))
            ).send_keys(name)

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class*='phone']"))
            ).send_keys(phone)

            logging.info("Форма успешно заполнена")
        except TimeoutException as e:
            logging.error(f"Не удалось заполнить форму в корзине: {e}")
            raise

    def submit_order(self):
        """Отправить заказ"""
        try:
            logging.info("Попытка отправить заказ")
            submit_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='fill']"))
            )
            submit_button.click()
            logging.info("Заказ успешно отправлен")
        except TimeoutException as e:
            logging.error(f"Не удалось отправить заказ: {e}")
            raise

    def is_cart_empty(self):
        """Проверить, что корзина пуста"""
        try:
            logging.info("Проверка, пуста ли корзина")
            empty_message = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#order-list h2"))
            )
            if "Корзина пуста" in empty_message.text:
                logging.info("Корзина пуста")
                return True
            return False
        except TimeoutException as e:
            logging.error(f"Не удалось проверить, пуста ли корзина: {e}")
            return False

    def remove_item_from_cart(self):
        """Удалить товар из корзины"""
        try:
            logging.info("Попытка удалить товар из корзины")
            remove_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick='deleteCardItem(this, 642)'] img"))
            )
            remove_button.click()
            logging.info("Товар успешно удален из корзины")
        except TimeoutException as e:
            logging.error(f"Не удалось удалить товар из корзины: {e}")
            raise


# Загружаем переменные из .env
load_dotenv()


class CartAPI:
    BASE_URL = "https://www.sibdar-spb.ru/ajax/basketOrder.php"

    @staticmethod
    def get_headers():
        """Возвращает заголовки из .env"""
        return {
            "accept": os.getenv("ACCEPT"),
            "content-type": os.getenv("CONTENT_TYPE"),
            "origin": os.getenv("ORIGIN"),
            "referer": os.getenv("REFERER"),
            "user-agent": os.getenv("USER_AGENT"),
            "x-requested-with": os.getenv("X_REQUESTED_WITH")
        }

    @staticmethod
    def get_cookies():
        """Возвращает куки из .env"""
        return {
            "CONSENT": os.getenv("CONSENT"),
            "basketor": os.getenv("BASKETOR"),
            "PHPSESSID": os.getenv("PHPSESSID"),
            "SLO_G_WPT_TO": os.getenv("SLO_G_WPT_TO"),
            "SLO_GWPT_Show_Hide_tmp": os.getenv("SLO_GWPT_Show_Hide_tmp"),
            "SLO_wptGlobTipTmp": os.getenv("SLO_wptGlobTipTmp")
        }

    @staticmethod
    def modify_cart(item_id, action):
        """Отправляет запрос на изменение содержимого корзины"""
        payload = (f"data=%7B%22idCookie%22%3A%22{os.getenv('BASKETOR')}%"
                   f"22%2C%22idProd%22%3A%22{item_id}%22%2C%22type%22%3A%22{action}%22%7D")
        response = requests.post(
            CartAPI.BASE_URL,
            data=payload,
            headers=CartAPI.get_headers(),
            cookies=CartAPI.get_cookies()
        )
        return response
