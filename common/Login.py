import os
import configparser
from selenium.webdriver.common.by import By
from selenium import  webdriver
from common.config_utils import config   #直接导入类的方法
from common import set_driver  ##自定义


def login(username,password):
    driver.get(config.get_url)
    driver.find_element(By.XPATH, '//input[@name="account"]').send_keys(config.get_user_name)
    driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys(config.get_password)
    driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()


if __name__ == '__main__':
    driver = set_driver.set_driver()
    driver.get(config.get_url)
    login(config.get_user_name,config.get_password)



