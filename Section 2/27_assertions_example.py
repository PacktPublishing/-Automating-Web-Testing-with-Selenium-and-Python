from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/se/page.html')
try:
    assert '404 Not Found' not in driver.page_source
except AssertionError:
    print('Error: page not found, check URL.')
driver.close()

