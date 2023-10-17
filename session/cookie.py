import requests
session = requests.Session()
print(session.cookies.get_dict())
session.get("https://www.naver.com/")
print(session.cookies.get_dict())
session.cookies.set("COOKIE_NAME","value",domain="naver.com")
print(session.cookies.get_dict())