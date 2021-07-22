# webdriver: 크롬 브라우저를 사용하여 브라우저 열기 위한 모듈
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 1. 크롬 브라우저 불러오기
driver= webdriver.Chrome()

# 2. 드라이버를 통해 불러오고자 하는 url 지정
url = "https://www.google.com"
driver.get(url)

# 3. 구글 검색 입력 란에 '파이썬' 키워드 입력 
# 조건은 class 로 구분함 (.), id는 (#)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')

# 4. 키보드 엔터키를 클릭
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

# 5. 세번째 검색 결과 요소를 찾아서 클릭... (클래스 속성)
driver.find_elements_by_css_selector('.LC20lb')[2].click()
