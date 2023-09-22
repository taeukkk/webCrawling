import requests
from bs4 import BeautifulSoup

URL = "https://crawlingstudy-dd3c9.web.app/02/"
response = requests.get(URL)
soup = BeautifulSoup(response.text,'html.parser')

# select: list 형태로 가져옴
result = soup.select("#title") #id 
result = soup.select("div") #tag
result = soup.select_one("div") 
result = soup.select(".blue") #class
result = soup.select("div#title.blue")
result = soup.select("a[href]") # attribute
result = soup.select("a[href$='.com']") #.com으로 끝나는
# print(result[0]) 
# print(result[0].text)

result = soup.select("div#winter p") #후손
result = soup.find(id="winter").find_all("p")

result = soup.select("div#winter > p") #자식
print(result)