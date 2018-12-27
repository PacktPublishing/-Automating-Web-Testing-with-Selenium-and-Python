import unittest
from selenium import webdriver
from page import LoginPage
from locators import CommonPageLocators
from locators import LoginPageLocators


class TestHRMBase(unittest.TestCase):
    """
    TBD
    """
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=chrome_options)


    def tearDown(self):
        self.driver.quit()


class TestLogin(TestHRMBase):
    """
    TBD
    """
    def setUp(self):
        super().setUp()
        self.login = LoginPage(self.driver)


    def test_TC_L_001(self):
        pass


    def test_TC_L_002(self):
        pass


    def test_TC_L_003(self):
        pass


if __name__ == '__main__':
    unittest.main()