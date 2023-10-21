from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymysql

db = pymysql.connect(host='localhost',port=3306,user='study',password='study',db='study')
cursor = db.cursor()

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://www.rocketpunch.com/jobs')
time.sleep(3)

for cur_page in range(1,4):
    for page in driver.find_elements(By.CSS_SELECTOR,'#pagination-wrapper > div > div.tablet.computer.large.screen.widescreen.only a'):
        if page.text == str(cur_page):
            page.send_keys(Keys.ENTER)
            time.sleep(3)
            
            for company in driver.find_elements(By.CSS_SELECTOR,'div#search-results div.company'):
                sql = """
                    INSERT INTO company2(name,description)
                        VALUES (%s,%s)
                """
                cursor.execute(sql,(company.find_element(By.CSS_SELECTOR,'div.company-name').text.strip(),
                    company.find_element(By.CSS_SELECTOR,'div.description').text.strip()))
                
                db.commit()
                company_id = cursor.lastrowid

                try:
                    more = company.find_element(By.CSS_SELECTOR,'a.more-jobs')
                    driver.execute_script('arguments[0].click()',more)
                    time.sleep(1)
                except:
                    pass

                for detail in company.find_elements(By.CSS_SELECTOR,'div.company-jobs-detail div.job-detail'):
                    sql = """
                        INSERT INTO job2(company_id, title, info, date)
                            VALUES(%s, %s, %s, %s)
                    """
                    
                    cursor.execute(sql,(company_id,
                        detail.find_element(By.CSS_SELECTOR,'div.job-name').text.strip(),
                        detail.find_element(By.CSS_SELECTOR,'div.job-stat-info').text.strip(),
                        detail.find_element(By.CSS_SELECTOR,'div.job-dates > span').text.strip()))

                    db.commit()
            # print("이동")
            break