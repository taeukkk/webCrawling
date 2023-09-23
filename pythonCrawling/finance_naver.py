import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/sise/sise_quant.nhn"
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

data = []
graph = []
for item in soup.select('table.type_2 tr'):
    if len(item.select('td')) !=12:
        continue
    tds = item.select('td')
    status = '-'
    if tds[3].select_one('img') != None:
        status = tds[3].select_one('img').attrs['alt']
    data.append({
        'num': tds[0].text,
        '종목명': tds[1].text,
        '현재가': tds[2].text,
        '전일비':tds[3].select_one('span').text.strip(),
        '등락여부': status
    })
    
print(data)

