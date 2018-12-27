from selenium import webdriver
import time 
driver = webdriver.Chrome()
driver.get('http://localhost/se/table.html')
time.sleep(3)

driver.find_element_by_xpath("//*[text()='Apple']/preceding-sibling::td/input").click()

driver.execute_script("document.body.style.zoom = '1.5'")
# driver.close()

