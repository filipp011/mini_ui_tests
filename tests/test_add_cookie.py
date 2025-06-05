from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Код, который добавляет куку
new_cookie = {"name": "my_first_cookie", "value": "15"}
driver.add_cookie(new_cookie)

# Проверка поля value для добавленной куки
cookie = driver.get_cookie("my_first_cookie")
assert cookie['value'] == '15'

driver.quit() 