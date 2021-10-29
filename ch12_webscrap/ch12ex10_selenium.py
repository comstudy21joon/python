# 1. 필요한 라이브러리 import
from bs4 import BeautifulSoup
# 크롬 드라이버를 사용하기 위해 import
from selenium import webdriver
# sleep 을 사용하기 위해 time 모듈 import
import time


# 2. 크롬드라이버 경로 설정하기, 웹브라우저 열기
path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com/')


# element 나 id 같은 것은 F12 로 개발자 도구를 켜서 찾는다
#driver.find_element_by_id("element_id").click()
driver.find_element_by_css_selector("ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a").click()
'''
element = driver.find_element_by_id("inp_search")
element.send_keys("키워드")
driver.find_element_by_link_text("검색").click()
'''