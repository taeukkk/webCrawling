import requests
from bs4 import BeautifulSoup
for i in range(1,11):
    URL = f"https://www.musinsa.com/ranking/best?period=now&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={i}&viewType=small&priceMin=&priceMax="
    response = requests.get(URL)
    soup = BeautifulSoup(response.text,"html.parser")
    print("PAGE ==========",i)
    rank = []
    for item in soup.select('#goodsRankList .li_box'):
        # re.findall('[0-9,]*원',item.select_one('.article_info p.price).text)
        price = item.select_one('.article_info p.price').text.strip().split(" ")
        info = {
            '브랜드': item.select_one('.article_info p.item_title').text.strip(),
            # '제품명': item.select_one('.list_info').text.strip(),
            '제품명': item.select_one('.article_info p.list_info a').attrs['title'],
            '가격': price[-1]
        }
        rank.append(info)
    print(rank)
