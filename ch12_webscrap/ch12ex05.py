import time
from SearchList import getSearchList

# 1초에 한번씩 갱신하고 싶다.
# 총 10회 갱신
for cnt in range(10):
    search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
    div_list = search_list[0].find_all('div', class_='hdline_article_tit')
    for i, element in enumerate(div_list):
        print(i, element.find('a').text.strip())

    time.sleep(10)
    print("{:-^50}".format("10초 한번씩 검색"))