#크롤링 하여 뉴스 내용 저장
import time
import requests
from SearchList import getSearchList
from Tools import replaceSRC

import pickle

imgList = []
with open("news/imgList.txt", "rb") as fp :
    imgList = pickle.load(fp)

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')
for i, element in enumerate(div_list):
    # 뉴스 링크를 타고 들어간다
    contentTags = getSearchList("https://news.naver.com" + element.find("a")["href"], "div#articleBodyContents")
    for j, newsContent in enumerate(contentTags) :
        with open("news/newsContent"+str(i)+str(j)+".html", "w", encoding="utf8") as fp :
            if len(imgList[i]) > 0 :
                newsContent = replaceSRC(str(newsContent), imgList[i])
                fp.write(newsContent)
            else :
                fp.write( str(newsContent) )