import requests
import json

# response = requests.get("https://crawlingstudy-dd3c9.web.app/05/")
response = requests.get("https://jsonplaceholder.typicode.com/photos")
datas = []
    
for idx,data in enumerate(response.json()):
    
    if idx ==1:
        break

    temp = {
        "id":data['id'],
        "title":data['title'],
        "comment":[]
    }
    comments = requests.get("https://jsonplaceholder.typicode.com/comments",params={
        "postId":data['id']
    })
    for comment in comments.json():
        temp["comment"].append(comment['body'])
    
    datas.append(temp)

with open("data.json","w") as json_file:
    json.dump(datas,json_file)

print(datas)