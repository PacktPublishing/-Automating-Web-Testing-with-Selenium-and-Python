from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/se/32.html')
driver.save_screenshot('/tmp/scr32_1.png')
driver.get_screenshot_as_file('/tmp/scr32_2.png')
driver.close()