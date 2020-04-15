import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner

from common import set_driver  ##自定义


class LoginOutCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=set_driver.set_driver()
        self.driver.get('http://127.0.0.1/zentao/user-login.html')

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    def test_login_out(self):
        self.driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys("201314ANQIER1")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[@class='user-name']").click()
        self.driver.find_element(By.XPATH, "//div[1]/div/div/div/ul/li/ul/li[13]/a").click()
        time.sleep(1)
        text2 = self.driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").text
        self.assertEqual(text2, "登录", "test_login_out案例执行失败")
        print("test2pass，退出成功")


if __name__ == '__main__':
    suite01=unittest.TestSuite()
    suite01.addTest(LoginOutCase('test_login_out'))
    #方式三：
    file=open('result.html','wb')
    html_runner=HTMLTestRunner.HTMLTestRunner( stream=file,
                                               title='new',
                                               description='描述')
    html_runner.run(suite01)
    file.close()
