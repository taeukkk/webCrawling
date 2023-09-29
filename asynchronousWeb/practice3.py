import re
import json
import requests
from bs4 import BeautifulSoup

URL = "https://n.news.naver.com/mnews/article/011/0003987613?sid=101"
headers = {
'Referer':
'https://n.news.naver.com/mnews/article/comment/011/0003987613?sid=101',
'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
}
response = requests.get(URL,headers = headers)
soup = BeautifulSoup(response.text,"html.parser")
news_id= re.search("[0-9]{3}\/[0-9]+",URL).group().split("/")

news = {
    "title" : soup.select_one('h2#title_area span').text,
    "body" : soup.select_one('article#dic_area').text,
    "reaction":{}
}

response = requests.get(f"https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B69146(period)%5D%7CNEWS%5Bne_{news_id[0]}_{news_id[1]}%5D%7CNEWS_MAIN%5Bne_{news_id[0]}_{news_id[1]}%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1695969082488")
for reaction in response.json()['contents'][1]['reactions']:
    code = reaction['reactionTypeCode']['description']
    count = reaction['count']
    news["reaction"][code] = count

# https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20230925155059&_callback=jQuery331044101573671527605_1695979887653&lang=ko&country=KR&objectId=news011%2C0003987613&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=5&currentPage=4&refresh=false&sort=FAVORITE&current=2682308113&prev=2682084903&moreParam.direction=next&moreParam.prev=100004i00005605mvbfmycethd&moreParam.next=100000000000005mvglrjkwr7t&includeAllStatus=true&_=1695979887660
# response = requests.get("https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_cv=20230925155059&lang=ko&country=KR&objectId=news011%2C0003987613&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=2&currentPage=1&refresh=false&sort=FAVORITE&current=2682236263&prev=2682084903&moreParam.direction=next&moreParam.prev=100004i00005605mvbfmycethd&moreParam.next=100000100000105mvery922yld&includeAllStatus=true&_=1695977866829",headers = headers)
# for comment in json.loads(response.text.replace('_callback(',"")[:-2])['result']['commentList']:
#     print(comment['contents'])
