from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Запустить сайт
driver.get("http://uitestingplayground.com/classattr")
sleep(5)

#Нахождение и нажатие на кнопку с классом btn-primary
button = driver.find_element(By.CSS_SELECTOR, ".byn-primary")
button.click()

#Обработка всплывающего окна с предупреждением
alert = driver.switch_to.alert
alert.accept()

#Запустить скрипт три раза подряд
for _ in range(3):
    button.click()
    alert = driver.switch_to.alert