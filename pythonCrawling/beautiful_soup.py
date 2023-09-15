import requests
from bs4 import BeautifulSoup
# HTML에서 손쉽게 원하는 데이터를 가져올 수 있도록 지원

URL = 'http://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

result = soup.find("p") # 가장 상단에 있는 태그 하나만
result = soup.find_all("p",limit=2) # 일치하는 모든 태그 <= limit개

# 옵션값에 따라
result = soup.find("th","tablehead")
result = soup.find("th",class_="tablehead")
result = soup.find("th",attrs={"class":"tablehead"})
result = soup.find("h1",attrs={"title":"welcome"})
result = soup.find(id="hello")
# print(result)

result = soup.find("table")
result2 = result.find("tbody")

result = soup.find("table").find("tbody")
# print(result2)

result = soup.find("a")
print(result.attrs['href'])
print(result.text) # tag 제거

print(result)