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
        self.login.assert_elem_text(LoginPageLocators.LOGIN_PANEL, 'LOGIN Panel')
        user_name_input = self.login.driver.find_element(*LoginPageLocators.USERNAME)
        self.assertEqual(user_name_input.tag_name, 'input')
        password_input = self.login.driver.find_element(*LoginPageLocators.PASSWORD)
        self.assertEqual(password_input.tag_name, 'input')
        self.login.is_clickable(LoginPageLocators.LOGIN_BUTTON)


    def test_TC_L_002(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, self.login.default_password)
        self.login.click(LoginPageLocators.LOGIN_BUTTON)
        self.assertTrue('dashboard' in self.login.driver.current_url)
        self.assertTrue('<h1>Dashboard</h1>' in self.login.driver.page_source)


    def test_TC_L_003(self):
        self.login.send_text(LoginPageLocators.USERNAME, self.login.default_username)
        self.login.send_text(LoginPageLocators.PASSWORD, 'password')
        self.login.click(LoginPageLocators.LOGIN_BUTTON)
        self.login.assert_elem_text(LoginPageLocators.SPAN_MSG, 'Invalid credentials')



if __name__ == '__main__':
    unittest.main()