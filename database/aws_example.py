# pip3 install boto3
# pip3 install awscli
# aws configure

import requests
import datetime
# import boto3
import json
from bs4 import BeautifulSoup

headers = {
'Referer':'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=283',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
}

# s3 = boto3.resource('s3')

date= datetime.datetime.strptime('20231020','%Y%m%d')
for i in range(7):
    date_str = date.strftime('%Y%m%d')
    news = []
    page = 1

    while True:
        print(date_str,page)

        url = f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=283&sid1=105&date={date_str}&page={page}"
        response = requests.get(url,headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        if str(page) != soup.select_one('div.paging strong').text.strip():
            break
        
        for news_data in soup.select("ul.type06 li"):
            news.append({
                "title":news_data.select("a")[-1].text.strip(),
                "body":news_data.select_one("span.lede").text.strip()
            })
        
        page+=1

    # s3.Bucket('bucket_name').put_object(Key=f'news/{date_str}.json',Body=json.dumps(news,ensure_ascii=False))
    date -= datetime.timedelta(days=1)