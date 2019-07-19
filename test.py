#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

browser = webdriver.Firefox()
browser.get(link)

# Ваш код, который заполняет обязательные поля
fieldName = browser.find_element_by_css_selector('input[placeholder="Введите имя"]')
fieldName.send_keys('Ivan')

fieldLastName = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"]')
fieldLastName.send_keys('Ivanov')

fieldEmail = browser.find_element_by_css_selector('input[placeholder="Введите Email"]')
fieldEmail.send_keys('ivanov@yandex.ru')

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

