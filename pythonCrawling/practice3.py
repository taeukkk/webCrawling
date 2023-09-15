import requests
from bs4 import BeautifulSoup

URL = 'http://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

for result in soup.find_all("a"):
    response = requests.get(URL + result.attrs['href'])
    soup = BeautifulSoup(response.text,"html.parser")
    print(soup.body.text.strip())
    # print(soup.find("p").text.strip())
