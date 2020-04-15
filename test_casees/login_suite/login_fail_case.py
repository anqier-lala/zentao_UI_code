import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner

from common import set_driver   ##自定义

class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = set_driver.set_driver()
        self.driver.get('http://127.0.0.1/zentao/user-login.html')


    def tearDown(self) -> None:
        pass


    def test_login_fail1(self):
        self.driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("admin1")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys("201314ANQIER1")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()
        time.sleep(3)
        alert = self.driver.switch_to.alert  # 切换到js弹窗
        value = alert.text
        self.assertEqual(value,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail1案例执行失败')




    def test_login_fail2(self):
        self.assertGreater(3,1)



if __name__ == '__main__':
    suite01=unittest.TestSuite()
    suite01.addTest(LoginFailCase('test_login_fail1'))
    suite01.addTest(LoginFailCase('test_login_fail2'))
    #方式三：
    file=open('result.html','wb')
    html_runner=HTMLTestRunner.HTMLTestRunner( stream=file,
                                               title='new',
                                               description='描述'
                                                )
    html_runner.run(suite01)
    file.close()