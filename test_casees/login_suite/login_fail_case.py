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
        pass


    def tearDown(self) -> None:
        pass


    def test_login_fail1(self):
        self.assertGreater(2, 1)

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