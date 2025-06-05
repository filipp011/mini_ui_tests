from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

driver.find_element(By.ID, "email").send_keys("Nis_22@gmail.com")

# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, "password").send_keys("558852")

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Найди кнопку, получи её текст и проверь, что он равен 'Выйти'
# Нашли кнопку Выйти и получили ее название
driver.find_element(By.CLASS_NAME, "header__logout").text 
# Проверили, что название на кнопке равно "Выйти"
assert driver.find_element(By.CLASS_NAME, "header__logout").text == "Выйти"

driver.quit()