import os
from selenium import webdriver

def set_driver():
    driver = webdriver.Chrome() ##driver.exe 已经放在python的安装目录下，所以一行即可。
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://127.0.0.1/zentao/user-login.html')
    return driver

