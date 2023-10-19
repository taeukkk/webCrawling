from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://crawlingstudy-dd3c9.web.app/03/')

popular = []
    
for item in driver.find_elements(By.CSS_SELECTOR,'ul#popularItemList li'):
    popular.append([item.find_element(By.CSS_SELECTOR,'a').text,
                    item.find_element(By.CSS_SELECTOR,'span').text.replace(',','')])
print(popular)

major = []
for item in driver.find_elements(By.CSS_SELECTOR,'ul.lst_major li'):
    major.append([item.find_element(By.CSS_SELECTOR,'a').text,
                      item.find_element(By.CSS_SELECTOR,'span').text.replace(',','')])
print(major)