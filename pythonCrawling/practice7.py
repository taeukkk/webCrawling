import requests
from bs4 import BeautifulSoup

URL = "https://crawlingstudy-dd3c9.web.app/03/"
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

result = []
for element in soup.select(".sale_box"):
    # print(element)
    name = element.select_one(".sale_tit").text.strip()
    price = element.select(".detail_info dd.txt")[0].select_one("strong").text.replace(',','')
    type = element.select(".detail_info dd.txt")[1].text.split('|')
    area = element.select(".detail_info dd.txt")[2].text.split('|')
    sales = {
        "이름": name,
        "분양가": price,
        "유형": type[0],
        "분양 유형": type[1],
        "세대수": area[0],
        "평형": area[1],
    }
    result.append(sales)
print(result)