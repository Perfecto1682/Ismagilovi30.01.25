import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def browser():
    # Настройки для запуска браузера с интерфейсом (не headless)
    options = Options()
    options.add_argument("--window-size=1920x1080")  # Задаем размер окна
    options.add_argument("--disable-gpu")  # Отключаем использование GPU

    # Создаем экземпляр браузера с использованием webdriver-manager
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)

    yield browser  # передаем браузер в тесты

    # Закрываем браузер после выполнения всех тестов
    browser.quit()
