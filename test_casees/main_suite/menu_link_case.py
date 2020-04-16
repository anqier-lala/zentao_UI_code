import os
import time
import unittest
import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver  #自定义的打开浏览器并使之最大化
from common.config_utils import config
from common import login  #自定义的登录方法

class Link_Succes(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=set_driver.set_driver()

    def tearDown(self) -> None:
        pass

    def test_link1_succes(self):
        self.assertGreater(4, 1)
        self.driver.get(config.get_url)
        time.sleep(2)
        login.login(self.driver,config.get_user_name, config.get_password)
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//div[@class="panel-title"]'),'最新动态'))


    def test_link2_succes(self):
        self.assertGreater(4, 1)


if __name__ == '__main__':
    print(config.get_user_name)
    print(config.get_password)

    suite01=unittest.TestSuite()
    suite01.addTest(Link_Succes('test_link1_succes'))


    #方式三：
    file=open('result.html','wb')
    html_runner=HTMLTestRunner.HTMLTestRunner( stream=file,
                                               title='new',
                                               description='描述')
    html_runner.run(suite01)
    file.close()
