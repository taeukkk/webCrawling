from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://www.jungle.co.kr/')
button = driver.find_element(By.CSS_SELECTOR,'div#existMore a#more')

cursor = 0    
datas = []
    
for _ in range(3):
    button.click()
    time.sleep(2)
    items = driver.find_elements(By.CSS_SELECTOR,'ul.thumb_list > li')
    cnt = len(items)
    for idx in range(cursor,cnt):
        # print(items[idx].text)
        datas.append({
            'title':items[idx].find_elements(By.CSS_SELECTOR, "spam.title").text,
            'category':items[idx].find_elements(By.CSS_SELECTOR, "a.thumb_cate").text
        })
    cursor = cnt
print(datas)
