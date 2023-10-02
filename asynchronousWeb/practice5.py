from bs4 import BeautifulSoup
import requests
import pymysql
import json
import re

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

page = 1
db = pymysql.connect(host='localhost', port=3306, user='study', password='study', db='study', charset='utf8')
cursor = db.cursor()

for i in range(10):
    page+=i
    response = requests.get(f"https://www.rocketpunch.com/api/jobs/template?page={page}")
    soup = BeautifulSoup(response.json()['data']['template'],'html.parser')
    
    for co in soup.select('div.company-list > div.company'):
        name = co.select_one('div.company-name').text.strip()
        description = co.select_one('div.description').text.strip()

        cursor.execute("""
            INSERT INTO company(name,description)
            VALUES(%s,%s)
        """,(name,description))
        db.commit()
        
        id = cursor.lastrowid
        for job in co.select('div.job-detail'):
            title = job.select_one('div.job-name').text.strip()
            title = deEmojify(title)
            info = job.select_one('div.job-stat-info').text
            info = deEmojify(info)
            date = job.select('div.job-dates span')[0].text.strip()
            sql = """
                INSERT INTO job(company_id, title, info, date)
                VALUES(%s,%s,%s,%s)
            """
            cursor.execute(sql,(id,title,info,date))
            db.commit()
            