from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.implicitly_wait(5) #비동기 대기
driver.get('https://crawlingstudy-dd3c9.web.app/05/')

lists = driver.find_elements(By.CSS_SELECTOR, 'div#post > div')

result = []

seq = 1
for idx in range(0,len(lists),2):
    lists[idx].click()
    time.sleep(1)

    data = {
        'id': seq,
        'title': lists[idx].text,
        'comments':[]
    }    
    
    comments = driver.find_elements(By.CSS_SELECTOR,f'#\\3{seq} > div')
    
    for i in range(1,len(comments),2):
        data['comments'].append(comments[i].text)
    
    result.append(data)
    seq+=1

with open('data.json','w') as json_file:
    json.dump(result, json_file)