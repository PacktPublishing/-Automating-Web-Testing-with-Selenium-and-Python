from selenium import webdriver
import time 
driver = webdriver.Chrome()
driver.get('http://localhost/se/31.html')
driver.execute_script("document.body.style.zoom = '1.7'")
time.sleep(1)
driver.execute_script('document.getElementById("demo").innerHTML = "JavaScript injection from Selenium";')
time.sleep(2)
driver.close()