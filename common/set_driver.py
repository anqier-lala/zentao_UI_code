import os
from selenium import webdriver

def set_driver():
    driver = webdriver.Chrome() ##driver.exe 已经放在python的安装目录下，所以一行即可。
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

