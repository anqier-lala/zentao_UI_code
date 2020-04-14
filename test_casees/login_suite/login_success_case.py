import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner

from common import set_driver  ##自定义


class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=set_driver.set_driver()
        self.driver.get('http://127.0.0.1/zentao/user-login.html')

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    def test_login_succes1(self):
        self.driver.find_element(By.XPATH, '//input[@name="account"]').send_keys('admin')
        self.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys('201314ANQIER1')
        self.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()
        actual=self.find_element(By.XPATH, "//span[@class='user-name']").text
        self.assertEqual(actual,'admin','test_login_succes1用例执行失败')

    def test_login_succes2(self):
        self.assertGreater(4, 1)

if __name__ == '__main__':
    suite01=unittest.TestSuite()
    suite01.addTest(LoginFailCase('test_login_succes1'))
    #方式三：
    file=open('result.html','wb')
    html_runner=HTMLTestRunner.HTMLTestRunner( stream=file,
                                               title='new',
                                               description='描述'
                                                )
    html_runner.run(suite01)
    file.close()
