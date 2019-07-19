#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

browser = webdriver.Firefox()
browser.get(link)

WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))

browser.find_element_by_id("book").click()

elementX = browser.find_element_by_id('input_value').text
answer = calc(elementX)

fieldAnswer = browser.find_element_by_id('answer')
fieldAnswer.send_keys(answer)

browser.find_element_by_id('solve').click()

