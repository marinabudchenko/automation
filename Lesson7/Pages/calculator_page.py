import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: bool):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def clear_fill_in_field(self, time):
        self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
        self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(time)

    def make_calculation(self):
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-primary"]'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="operator btn btn-outline-success"]'
            ).click()
        self._driver.find_element(
            By.XPATH, '(//span[@class="btn btn-outline-primary"])[2]'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, 'span[class="btn btn-outline-warning"]'
            ).click()


    with allure.step("Вызов метода для получения результата сложения"):
        def get_result(self):
            WebDriverWait(self._driver, "48").until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
            return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text == "15"

    with allure.step("Закрытия драйвера веб-браузера"):
        def close_driver(self):
            self._driver.quit()
