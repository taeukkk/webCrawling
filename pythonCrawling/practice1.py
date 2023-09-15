import requests
from bs4 import BeautifulSoup

URL = 'http://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

result = soup.find(id="cook")
print(result.text)
