from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# import json
# import boto3

#s3 = boto3.resource('s3')

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=226&sid1=105&date=20231020')

news_all = []

items = driver.find_elements(By.CSS_SELECTOR,"div.list_body > ul > li")
item_cnt = len(items)
    
for i in range(item_cnt):
    items = driver.find_elements(By.CSS_SELECTOR,"div.list_body > ul > li")
    items[i].find_element(By.CSS_SELECTOR,"a").click()
    time.sleep(1)

    news_data = {
        'likeit' : [],
        'reply' : []
    }

    news_data['title'] = driver.find_element(By.CSS_SELECTOR,'h2#title_area').text
    news_data['body'] = driver.find_element(By.CSS_SELECTOR,'div#newsct_article').text.strip().replace('\n','')

    driver.find_element(By.CSS_SELECTOR,'#commentFontGroup > div.media_end_head_info_variety_likeit._LIKE_HIDE.as_likeit_improve > div > a').click()
    time.sleep(1)

    for reaction in driver.find_elements(By.CSS_SELECTOR,'#commentFontGroup > div.media_end_head_info_variety_likeit._LIKE_HIDE.as_likeit_improve > div > ul > li.u_likeit_list'):
        news_data['likeit'].append({
            'name':reaction.find_element(By.CSS_SELECTOR,'a.u_likeit_list_button > span.u_likeit_list_name').text,
            'count':reaction.find_element(By.CSS_SELECTOR,'span.u_likeit_list_count').text
        })
    
    try:
        driver.find_element(By.CSS_SELECTOR,'#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_new > div.u_cbox_view_comment > a > span.u_cbox_in_view_comment').click()
        time.sleep(0.5)

        idx = 0
        
        while True:  
            reply = driver.find_elements(By.CSS_SELECTOR,'#cbox_module_wai_u_cbox_content_wrap_tabpanel > ul > li')
            
            try:
                for i in range(idx,len(reply)):
                    try:
                        news_data['reply'].append(reply[i].find_element(By.CSS_SELECTOR,'span.u_box_contents').text.strip())
                    except:
                        pass
                driver.find_element(By.CSS_SELECTOR,'#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_paginate > a > span > span > span.u_cbox_page_more').click()
                time.sleep(0.2)
            except:
                break
            
            idx = len(reply)
            
        driver.back()
        time.sleep(0.5)
    except:
        pass

    driver.back()
    time.sleep(0.5)

    news_all.append(news_data)
    driver.back()
    time.sleep(0.5)
    print('')
    # if i==9:
    #     break

# s3.Bucket('bucket_name').put_object(Key=f'selenium/news.json',Body=json.dumps(new_all,ensure_ascii=False))