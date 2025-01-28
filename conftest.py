import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    # Настройки для запуска в фоновом режиме (headless)
    options = Options()
    options.add_argument("--headless")  # Запуск без интерфейса
    options.add_argument("--window-size=1920x1080")  # Задаем размер окна
    options.add_argument("--disable-gpu")  # Отключаем использование GPU

    # Создаем экземпляр браузера с опциями
    browser = webdriver.Chrome(options=options)
    yield browser  # передаем браузер в тесты
    browser.quit()  # закрываем браузер после выполнения всех тестов
