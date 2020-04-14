import os
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import set_driver  ##自定义


class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_link_succes1(self):
        self.assertEqual(1, 1)

    def test_link_succes2(self):
        self.assertGreater(4, 1)

