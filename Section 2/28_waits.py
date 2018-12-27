from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/se/28_waits.html')

# implicit wait
# driver.implicitly_wait(3)
# elem = driver.find_element_by_css_selector('p')

# explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p")))

print('Found element with text: {}'.format(elem.get_attribute('innerHTML')))
driver.close()
