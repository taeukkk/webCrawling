import requests
import datetime
from bs4 import BeautifulSoup

headers = {
'Referer':'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=283',
'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
}

date = datetime.datetime.strptime('20230929','%Y%m%d')
for i in range(5):#29일-25일
    print("=====",date,"=====")
    page = 1
    while True:
        date_str = date.strftime('%Y%m%d')
        URL = f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=283&sid1=105&date={date_str}&page={page}"
        response = requests.get(URL,headers = headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        if str(page)!= soup.select_one('div.paging > strong').text:
            print('DONE')
            break
        print("=====",page,"=====")
        for news_item in soup.select("div.list_body ul li"):
            news_url = ''
            try:
                news_url = news_item.select("dt")[1].select_one('a').attrs['href']
            except:
                news_url = news_item.select("dt")[0].select_one('a').attrs['href']
            response = requests.get(news_url)
            news_soup = BeautifulSoup(response.text,"html.parser")

            print(news_soup.select_one('div.media_end_head_title').text.strip())#제목
            print(news_soup.select_one('article#dic_area').text)#내용
        page+=1
    date = date - datetime.timedelta(days=1)