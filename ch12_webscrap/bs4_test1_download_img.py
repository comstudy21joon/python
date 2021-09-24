#크롤링 하여 이미지 저장
import requests, json

from SearchList import getSearchList
from ReplaceSrc import replaceSRC

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')
newsList = []

filePath = "C:\\Users\\KBJ\Documents\\_NodeJS_NodeJsExample\\NodeJS_And_Python_scrab\\public\\";

# 이미지 저장
for i, element in enumerate(div_list):
    newsObj = {}
    newsObj['newsLink'] = "https://news.naver.com" + element.find("a")["href"]
    imgTags = getSearchList(newsObj['newsLink'], "div#articleBodyContents img")
    contentTags = getSearchList(newsObj['newsLink'], "div#articleBodyContents")

    images = []
    for j, img in enumerate(imgTags) :
        src = img.get("src")
        response = requests.get(src[:src.index("?")] )
        assert response.status_code is 200

        imgUrl = "newImg"+str(i)+str(j)+".jpg"
        images.append("./"+imgUrl)
        with open(filePath + imgUrl, "wb") as fp :
            fp.write(response.content)

    newsObj['images'] = images

    for j, newsContent in enumerate(contentTags) :
        with open(filePath + "newsContent"+str(i)+str(j)+".html", "w", encoding="utf8") as fp :
            if len(newsObj['images']) > 0 :
                newsContent = replaceSRC(str(newsContent), newsObj['images'])
                fp.write(newsContent)
            else :
                fp.write( str(newsContent) )

    newsList.append(newsObj)

print(newsList)

with open(filePath + "newsList.json", "w", encoding="utf8") as fp :
    json.dump(newsList, fp)