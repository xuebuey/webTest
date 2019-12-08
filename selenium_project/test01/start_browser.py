# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
title = EC.title_contains('注册')
# element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, 'controls')
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
email_element = driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("lx@163.com")
print(email_element.get_attribute("value"))
driver.close()

#driver.find_element_by_id("register_email").send_keys('lx948008@163.com')
#driver.find_element_by_id("register_nickname").send_keys("lixue")
#driver.find_element_by_id("register_password").send_keys("sangfor123")
#driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("123456")
