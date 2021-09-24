import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/")
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

search_list = dom.select("ul.hdline_article_list")
#print(search_list)
a_list = search_list[0].find_all('div', class_='hdline_article_tit')
for i, element in enumerate(a_list):
    print(i, element.find('a').text.strip())