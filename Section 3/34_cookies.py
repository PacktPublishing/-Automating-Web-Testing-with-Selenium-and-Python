from selenium import webdriver
import time 

def displayCookies():
    all = ''
    for c in driver.get_cookies():
        all += c['name'] + ' : ' + c['value'] + '\n'
    return all

driver = webdriver.Chrome()
driver.get('http://localhost/se/34.html')
driver.delete_all_cookies()
driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
print('Cookies:\n{}'.format(displayCookies()))
driver.find_element_by_id('john').click()
print('Cookies:\n{}'.format(displayCookies()))
driver.find_element_by_id('doe').click()
print('Cookies:\n{}'.format(displayCookies()))
print('Cookies:\n{}'.format(driver.get_cookies()))
driver.close()