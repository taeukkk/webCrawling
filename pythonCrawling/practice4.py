import requests
from bs4 import BeautifulSoup

URL = "https://crawlingstudy-dd3c9.web.app/03/"
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

popular,major = [],[]
for element in soup.select(".lst_pop > li"):
    name = element.select_one('a').text
    price = element.select_one('span').text
    popular.append([name,price])
for element in soup.select(".lst_major > li"):
    name = element.select_one('a').text
    price = element.select_one('span').text
    major.append([name,price])
print(popular)
print(major)
