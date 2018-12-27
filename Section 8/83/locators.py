from selenium.webdriver.common.by import By


class CommonPageLocators:
    ADMIN = (By.ID, 'menu_admin_viewAdminModule')


class LoginPageLocators:
    LOGIN_PANEL = (By.ID, 'logInPanelHeading')
    USERNAME = (By.ID, 'txtUsername')
    PASSWORD = (By.ID, 'txtPassword')
    LOGIN_BUTTON = (By.ID, 'btnLogin')
    SPAN_MSG = (By.ID, 'spanMessage')


class AdminPageLocators:
    JOB = (By.ID, 'menu_admin_Job')
    JOB_TITLES = (By.ID, 'menu_admin_viewJobTitleList')
    JOB_TITLE_ADD_BTN = (By.ID, 'btnAdd')
    JOB_TITLE_JT_FIELD = (By.ID, 'jobTitle_jobTitle')
    JOB_TITLE_JD_FIELD = (By.ID, 'jobTitle_jobDescription')
    JOB_TITLE_SAVE_BTN = (By.ID, 'btnSave')
    JOB_TITLE_TABLE = (By.ID, 'resultTable')
    JOB_WORKSHIFT = (By.ID, 'menu_admin_workShift')
    JOB_WORKSHIFT_ADD_BTN = (By.ID, 'btnAdd')
    JOB_WORKSHIFT_NAME = (By.ID, 'workShift_name')
    JOB_WORKSHIFT_TO_HOUR = (By.ID, 'workShift_workHours_to')
    JOB_WORKSHIFT_SAVE_BTN = (By.ID, 'btnSave')
    JOB_WORKSHIFT_TABLE = (By.ID, 'resultTable')