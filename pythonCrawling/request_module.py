import requests

# URL = 'http://httpbin.org/get'
URL = 'http://httpbin.org/post'
#http://httpbin.org/get?key1=value1&key2=value2처럼 주소로 파라미터를 보낼 수도 있음

params = {'data1':'data1','data2':'data2'}
headers = {'Content-Type':'application/json; charset=utf-8','test':'test'}
data = {'data1':'data1','data2':'data2'}
# response = requests.get(URL)
# response = requests.get(URL,params=params,headers=headers)
response = requests.post(URL,params=params,headers=headers,data=data)
print(response.text)

# response = requests.post('http://httpbin.org/post')

# print(response.status_code)
# print(response.text)
