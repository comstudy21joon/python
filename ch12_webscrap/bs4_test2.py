import requests
from SearchList import getSearchList
from Tools import replaceSRC

import json

savePath = "D:\\node_work2\\public\\news\\"

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')

newsList = []

for i, element in enumerate(div_list):
    newsObj = {}
    newsLink = "https://news.naver.com"
    newsUrl = newsLink + element.find("a")["href"]
    newsTit = element.find("a").text.strip()

    imgTags = getSearchList(newsUrl, "div#articleBodyContents img")
    newsContents = getSearchList(newsUrl, "div#articleBodyContents")[0]

    srcList = []
    for j, img in enumerate(imgTags):
        src = img.get("src")
        response = requests.get(src[:src.index("?")])
        assert response.status_code is 200

        imgName = "tmp_img" + str(i) + str(j) + ".jpg"
        srcList.append(imgName)
        with open(savePath+imgName, "wb") as fp:
            fp.write(response.content)

    newsContents = replaceSRC(str(newsContents), srcList)
    contentsFile = "newsContent"+str(i)+".html"
    with open(savePath+contentsFile, "w", encoding="utf8") as fp :
        fp.write(newsContents)

    newsObj['title'] = newsTit
    newsObj['link'] = newsUrl
    newsObj['images'] = srcList
    #newsObj['contents'] = newsContents
    newsObj['contentsFile'] = contentsFile

    newsList.append(newsObj);


with open(savePath+"newsList.json", "w") as fp :
    json.dump(newsList, fp)
