from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/signin")

# Найди кнопку и кликни по ней
driver.find_element(By.CSS_SELECTOR, "[class='auth-form__button']").click

driver.quit()