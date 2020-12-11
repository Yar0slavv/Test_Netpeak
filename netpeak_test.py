from selenium import webdriver
import random
import time
import os
from selenium.webdriver.support.select import Select
from random import randint
import pytest

        
driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.implicitly_wait(20)
driver.maximize_window()


driver.get('https://netpeak.ua/')
driver.find_element_by_xpath('//li[@class="blog"]/a').click()
driver.find_element_by_xpath('//a[@class="btn green-btn"]').click()


driver.get('https://career.netpeak.ua/hiring/')
driver.find_element_by_name('up_file').send_keys("C:\programing\Selenium_Python\seleniumproject\pic.png")
time.sleep(5)
error_string_upfile = driver.find_element_by_xpath('//div[@id="up_file_name"]/label[@class="control-label"]').text
assert error_string_upfile == 'Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).'

nameList = ["Ivan", "Nicolas","Pablo", "Nicol"]
lastNameList = ["Petrov", "Askobar","Ivanov", "Moisha"]

firstBlockEmail = ''
for x in range(12):
    firstBlockEmail = firstBlockEmail + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

email = '@gmail.com'
operator = (73,66,68,97,96,99,63,93,67)
phone = ('+380'+ str(random.choice(operator)))

driver.find_element_by_id('inputName').send_keys(random.choice(nameList))
driver.find_element_by_id('inputLastname').send_keys(random.choice(lastNameList))
driver.find_element_by_id('inputEmail').send_keys(firstBlockEmail + email)
driver.find_element_by_id('inputPhone').send_keys(phone + str(random.randint(1000000,9999999)))


year = Select(driver.find_element_by_name('by'))
month = Select(driver.find_element_by_name('bm'))
day = Select(driver.find_element_by_name('bd'))


year.select_by_index(randint(0, len(year.options) - 1))
month.select_by_index(randint(0, len(month.options) - 1))
day.select_by_index(randint(0, len(day.options) - 1))

driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(5)

color_warning_fild = driver.find_element_by_xpath('//p[contains(@class,"warning-fields")]').value_of_css_property('color')         
assert color_warning_fild == 'rgba(255, 0, 0, 1)', 'Border does not highlight'


driver.find_element_by_xpath('//li[@class="blog"]/a').click()
page_check = driver.find_element_by_xpath('//h1').text
assert page_check == 'Курсы', 'Page "Курсы" does not open'


driver.quit()







