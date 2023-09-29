import requests
import json

# response = requests.get("https://crawlingstudy-dd3c9.web.app/04/")
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# datas = response.json()
# for data in datas:
#     print(data['title'])
#     print(data['body'])
#     print("")

datas = json.loads(response.text)
print(json.dumps(datas))#문자열로 변환
with open("data.json","w") as json_file:
    json.dump(datas, json_file)#파일에 저장



