from selenium import webdriver
import time 
driver = webdriver.Chrome()
driver.get('http://python.org')
time.sleep(1)
driver.maximize_window() 
driver.find_element_by_css_selector('a[title="Python Package Index"]').click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.close()