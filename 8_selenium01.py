# selenium: 브라우저 자동화 모듈
# webdriver: 크롬 드라이버 를 사용하여 브라우저 열기
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 웹 드라이버 불러오기
driver = webdriver.Chrome()

# 드라이버를 통해 불러오고자 하는 url 지정
url = 'https://www.google.com/'
driver.get(url)

# 1. 구글 검색 입력 란에 '파이썬' 키워드  입력 후 (F12 개발자 모드로 소스 확인 후, 조건은 class(.) 으로 구분함)
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')

# 2. 키보드 엔터키를 클릭 
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

# 3. 첫번째 검색 결과 하나의 요소를 찾고(클래스속성으로 ) (find_element()단수함수를 사용),  클릭
# driver.find_element_by_css_selector('.LC20lb').click()

# 4. 3번째 검색 결과 클릭
driver.find_elements_by_css_selector('.LC20lb')[2].click()
