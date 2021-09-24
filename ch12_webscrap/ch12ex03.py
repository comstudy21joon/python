import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com/")
assert response.status_code is 200
# bytes타입과 str 타입
print(type(response.content))
print(type(response.text))

dom = BeautifulSoup(response.content, "html.parser")
# BeautifulSoup 타입
print(type(dom))
# Tag 타입과 NaviableString 타입
print(dom.title)
print(dom.title.string)
print(type(dom.title))
print(type(dom.title.string))