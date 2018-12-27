from selenium.webdriver.common.by import By


class CommonPageLocators:
    pass


class LoginPageLocators:
    LOGIN_PANEL = (By.ID, 'logInPanelHeading')
    USERNAME = (By.ID, 'txtUsername')
    PASSWORD = (By.ID, 'txtPassword')
    LOGIN_BUTTON = (By.ID, 'btnLogin')
    SPAN_MSG = (By.ID, 'spanMessage')
