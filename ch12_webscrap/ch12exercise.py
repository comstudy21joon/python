"""
import requests
from bs4 import BeautifulSoup

response = requests.get("https://ko.wikipedia.org/wiki/%EA%B0%95%EC%95%84%EC%A7%80")
assert response.status_code is 200

dom = BeautifulSoup(response.content, "html.parser")

img_list = dom.select("#content img")

for i, img in enumerate(img_list) :
    img_src = "https:" + img.get('src')

    resp2 = requests.get(img_src)
    assert response.status_code is 200

    file_name_start = img_src.rindex('/')

    if img_src[-4:].lower() == '.jpg' or img_src[-4:].lower() == '.png' :
        new_file_name = img_src[file_name_start:]
        if len(new_file_name) > 20 :
            new_file_name =  new_file_name[-20:]
        new_file_name = str(i) + new_file_name
        try :
            print(new_file_name)
            with open("wiki_img/"+ new_file_name, "wb") as fp:
                fp.write(resp2.content)
        except :
            pass
"""


"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time

path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com/')

search = driver.find_element_by_css_selector("#query")
search.send_keys("딥러닝")
driver.find_element_by_id("search_btn").click()

driver.implicitly_wait(3)
driver.find_element_by_css_selector("div.lnb_menu ul.base li.lnb3").click()
"""


"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time

path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com/')

search = driver.find_element_by_css_selector("#query")
search.send_keys("딥러닝")
driver.find_element_by_id("search_btn").click()

driver.implicitly_wait(3)
driver.find_element_by_css_selector("div.lnb_menu ul.base li.lnb3").click()

driver.implicitly_wait(3)
result_area = driver.find_element_by_id("elThumbnailResultArea")
blog_titles = result_area.find_elements_by_css_selector("li dl dt .sh_blog_title")
for i, title in enumerate(blog_titles) :
    print(i, title.text)
    print(title.get_attribute('href'))
"""

"""
from selenium import webdriver

path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com/')

link_login = driver.find_element_by_css_selector("#account a.link_login")
link_login.click()
driver.implicitly_wait(3)

id = driver.find_element_by_css_selector("input#id.int")
id.send_keys("naver_id")
pw = driver.find_element_by_css_selector("input#pw.int")
pw.send_keys("naver_pwd")
driver.find_element_by_css_selector("input#log\.login").click()

"""


from selenium import webdriver

path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://www.kocw.net/home/index.do')

search = driver.find_element_by_css_selector("input#query.searchTxt")
search.send_keys("딥러닝")
driver.find_element_by_css_selector("input.searchBtn").click()

contentWrap = driver.find_element_by_css_selector("div.lectureContentWrap")
content_info_list = contentWrap.find_elements_by_css_selector("dl.listWrap2 dl");
for content_info in content_info_list :
    title = content_info.find_element_by_css_selector("dt strong a").text
    univ = content_info.find_element_by_css_selector("span.first-child").text
    print("%s (%s)" %(title, univ))


