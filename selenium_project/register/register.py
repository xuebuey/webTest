# coding=utf-8
from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 初始化浏览器
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

# 获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

# 获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890qwertyuiasdgg', 8))
    return user_info
title = EC.title_contains('注册')
# element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, 'controls')
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
email_element = driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("lx@163.com")
print(email_element.get_attribute("value"))
driver.close()
