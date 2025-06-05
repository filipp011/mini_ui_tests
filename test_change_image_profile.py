from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
driver.find_element(By.ID, "email").send_keys("Nis_22@gmail.com")
driver.find_element(By.ID, "password").send_keys("558852")
driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

# Добавь явное ожидание загрузки страницы
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Кликни по изображению профиля
driver.find_element(By.XPATH,".//div[@class='profile__image']" ).click()

# В поле ссылки на изображение введи ссылку, используй переменную avatar_url
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Сохрани новое изображение
driver.find_element(By.XPATH, ".//button[@class='button popup__button' and text()='Сохранить']")

# Запиши в переменную style значение атрибута style для элемента с изображением профиля
style = driver.find_element(By.XPATH,".//div[@class='profile__image']" ).get_attribute('style')
# Проверь, что в style содержится ссылка на аватар
assert avatar_url in style

driver.quit()