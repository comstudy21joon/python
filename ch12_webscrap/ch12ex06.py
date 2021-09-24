#크롤링 하여 이미지 저장
import requests
from SearchList import getSearchList
import pickle

search_list = getSearchList("https://news.naver.com/", "ul.hdline_article_list")
div_list = search_list[0].find_all('div', class_='hdline_article_tit')
imgList = []
for i, element in enumerate(div_list):
    imgTags = getSearchList("https://news.naver.com" + element.find("a")["href"], "div#articleBodyContents img")

    images = []
    for j, img in enumerate(imgTags) :
        src = img.get("src")
        response = requests.get(src[:src.index("?")] )
        assert response.status_code is 200

        imgUrl = "newImg"+str(i)+str(j)+".jpg"
        images.append("./"+imgUrl)
        with open("news/"+imgUrl, "wb") as fp :
            fp.write(response.content)

    imgList.append(images)

print(imgList)

with open("news/imgList.txt", "wb") as fp :
    pickle.dump(imgList, fp)