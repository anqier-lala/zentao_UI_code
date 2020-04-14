import os
import configparser
from selenium.webdriver.common.by import By
from selenium import  webdriver
from common.config_utils import config   #直接导入类的对象


def login(driver,username,password):
    driver.find_element(By.XPATH, '//input[@name="account"]').send_keys(config.get_user_name)
    driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys(config.get_password)
    driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()

if __name__ == '__main__':
    print(config.get_user_name)
    print(config.get_password)

