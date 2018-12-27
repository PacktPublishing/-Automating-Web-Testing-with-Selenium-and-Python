import unittest
from selenium import webdriver
from page import LoginPage
from locators import CommonPageLocators
from locators import LoginPageLocators
from locators import AdminPageLocators


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


    @unittest.skip('not needed, already tested in other TCs')
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


class TestAdmin(TestHRMBase):


    @classmethod
    def setUpClass(cls):
        super().setUp(cls)
        cls.login = LoginPage(cls.driver)
        cls.login.login()
        cls.page = cls.login


    def test_TC_A_001(self):
        """
        Add new job title | Navigating to Admin > Job > Job Titles and fill in the form to add new job title.
        """
        job_title = 'QA automation developer'
        job_description = 'Automating tests in Python and Selenium Webdriver.'
        self.page.hover_to(CommonPageLocators.ADMIN)
        self.page.hover_to(AdminPageLocators.JOB)
        self.page.click(AdminPageLocators.JOB_TITLES)
        self.page.click(AdminPageLocators.JOB_TITLE_ADD_BTN)
        self.page.send_text(AdminPageLocators.JOB_TITLE_JT_FIELD, job_title)
        self.page.send_text(AdminPageLocators.JOB_TITLE_JD_FIELD, job_description)
        self.page.click(AdminPageLocators.JOB_TITLE_SAVE_BTN)
        table = self.page.get_elem(AdminPageLocators.JOB_TITLE_TABLE)
        assert job_title in table.get_attribute('innerHTML')


    def test_TC_A_002(self):
        """
        Add new work shift | Navigating to Admin > Job > Work Shifts and add new work shift.
        """
        shift_title = 'QA short shift'
        shift_end = '13:00'
        self.page.hover_to(CommonPageLocators.ADMIN)
        self.page.hover_to(AdminPageLocators.JOB)
        self.page.click(AdminPageLocators.JOB_WORKSHIFT)
        self.page.click(AdminPageLocators.JOB_WORKSHIFT_ADD_BTN)
        self.page.send_text(AdminPageLocators.JOB_WORKSHIFT_NAME, shift_title)
        self.page.choose(AdminPageLocators.JOB_WORKSHIFT_TO_HOUR, shift_end)
        self.page.click(AdminPageLocators.JOB_WORKSHIFT_SAVE_BTN)
        table = self.page.get_elem(AdminPageLocators.JOB_WORKSHIFT_TABLE)
        assert shift_title in table.get_attribute('innerHTML')


    @classmethod
    def tearDownClass(cls):
        super().tearDown(cls)


if __name__ == '__main__':
    unittest.main()