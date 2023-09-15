import requests
from bs4 import BeautifulSoup

URL = 'http://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

key,value = [],[]
for result in soup.find("table").find_all("th"):
    key.append(result.text)
# for result in soup.find("table").find_all("td"):
#     value.append(result.text)
for element in soup.find("table").find("tbody").find_all("tr"):
    temp = []
    for td_element in element.find_all('td'):
        temp.append(td_element.text)
    value.append(dict(zip(key,temp)))
print(value)

# result = []
# for i in range(len(key)):
#     result.append({})
# for i in range(len(value)):
#     result[i//2][key[i%2]]=value[i]
# print(result)