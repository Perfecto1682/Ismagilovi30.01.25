import logging
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', force=True)


class CartPage:
    """Класс для работы с корзиной"""

    URL = "https://www.sibdar-spb.ru/"

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открыть главную страницу"""
        try:
            logging.info(f"Открытие страницы: {self.URL}")
            self.browser.get(self.URL)
            WebDriverWait(self.browser, 40).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            logging.info("Страница успешно загружена")
        except TimeoutException as e:
            logging.error(f"Не удалось открыть страницу {self.URL}: {e}")
            raise

    @allure.step("Выбрать категорию товаров")
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

    @allure.step("Добавить товар в корзину")
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

    @allure.step("Открыть корзину")
    def open_cart(self):
        """Открыть корзину"""
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

    @allure.step("Заполнить форму в корзине")
    def fill_in_cart_form(self, name, phone):
        """Заполнить форму в корзине"""
        try:
            logging.info(f"Заполнение формы: Имя - {name}, Телефон - {phone}")

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

    @allure.step("Отправить заказ")
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

    @allure.step("Проверить, пуста ли корзина")
    def is_cart_empty(self):
        """Проверить, что корзина пуста"""
        try:
            logging.info("Проверка, пуста ли корзина")
            empty_message = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#order-list h2"))
            )
            if "Корзина пуста" in empty_message.text:
                logging.info("Корзина действительно пуста")
                return True
            logging.info("Корзина не пуста")
            return False
        except TimeoutException as e:
            logging.error(f"Не удалось проверить, пуста ли корзина: {e}")
            return False

    @allure.step("Удалить товар из корзины")
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
