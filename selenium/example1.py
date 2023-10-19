from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

#1
driver.get('https://crawlingstudy-dd3c9.web.app/01/')
element = driver.find_element(By.CSS_SELECTOR,'p#hello')
print(element.text)
elements = driver.find_elements(By.CSS_SELECTOR,'p')
print(elements)

element = driver.find_element(By.CSS_SELECTOR,'table')
for item in driver.find_elements(By.CSS_SELECTOR,'tr'):
    print(item)
    print('')

element = driver.find_element(By.CSS_SELECTOR,'a')
print(element.get_attribute('href'))

#2
driver.get('https://www.base64decode.org/')
element = driver.find_element(By.CSS_SELECTOR,'#input')
element.send_keys('Python')
button = driver.find_element(By.CSS_SELECTOR,'#submit_text')
button.click()
time.sleep(30)

#3
driver.get('https://www.jungle.co.kr/')
elements = driver.find_elements(By.CSS_SELECTOR,'li')
print(len(elements))

button = driver.find_element(By.CSS_SELECTOR,'#more')
button.click()
time.sleep(2)

elements = driver.find_elements(By.CSS_SELECTOR,'li')
print(len(elements))
