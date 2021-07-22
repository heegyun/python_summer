from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
# 크롬 드라이버로 구글 열기
driver = webdriver.Chrome()
url= "https://www.google.com"
driver.get(url)

# 크게 브라우저 열기
driver.maximize_window()
action = ActionChains(driver)

# 로그인 버튼 찾기 id로 찾기 이때는 #을 사용
driver.find_element_by_css_selector('#gb_70').click()
time.sleep(2)
# gmail 로그인을 위해 id 입력창에 입력하기
action.send_keys('yhg1124@hnu.kr').perform() 
# 하나의 액션을 끝내고 다시 리셋을 하다.
action.reset_actions()

# 다음 버튼 클릭하기
driver.find_element_by_css_selector('.FliLIb').click()

time.sleep(2)
# 비밀번호 입력 후 
driver.find_element_by_css_selector('.whsOnd').send_keys('yhg1124*75')
# 다음 버튼 자동클릭
driver.find_element_by_css_selector('.FliLIb.DL0QTb').click()
time.sleep(2)
# 로그인 완료

# gmail   화면으로 이동
driver.get('https://mail.google.com/mail/u/0/?ogbl#inbox')
time.sleep(2)

# 편지 쓰기 자동 클릭
driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click() 
time.sleep(1)


action=ActionChains(driver) 

# 보내기 버튼 으로 가서 클릭이 안되는 요소라 하더라고  클릭 기능이 가능
send_btn = driver.find_element_by_css_selector('.gU.Up')

# 받는이, 제목, 내용 자동 입력 action chain처럼 입력해줌.(tab키 눌러서 이동하는 것처럼 구현)

(
action.send_keys('yhg1124@hnu.kr').key_down(Keys.ENTER).pause(2).key_down(Keys.TAB)
.send_keys('제목입니다.').pause(2).key_down(Keys.TAB)
.send_keys('abcde').pause(2).key_down(Keys.ENTER)
.key_down(Keys.SHIFT).send_keys('abcde').key_up(Keys.SHIFT).pause(2)
.move_to_element(send_btn).click()
.perform()
)


