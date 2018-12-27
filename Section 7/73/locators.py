from selenium.webdriver.common.by import By

class CommonPageLocators:
    SEARCH_BAR = (By.ID, "id-search-field")
    SEARCH_GO_BUTTON = (By.ID, "submit")
    DOC = (By.ID, "documentation")
    PY3_DOC_BUTTON = (By.CSS_SELECTOR, "#documentation > ul > li.tier-2.super-navigation > p.download-buttons > a:nth-child(1)")
    SEARCH_RESULT_LIST = (By.XPATH, "//h3[text()='Results']/following-sibling::ul")
    MAIN_MENU = (By.ID, "mainnav")

class AboutPageLocators:
    UPCOMING_EVENTS = (By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > h2')
    