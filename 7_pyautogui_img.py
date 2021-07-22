import pyautogui

# print(pyautogui.position())
# pyautogui.moveTo(437,49)
# pyautogui.click(437,49)

# 예 2-1 좌표가 아니라 이미지 인식을 해서 좌표를 대신한다.
# 계산기 실행 
# pip install opencv-python 설치
# 같은 경로에 이미지 존재해야 함
# 해당 이미지가 있는 좌표와 크기를 반환
# i = pyautogui.locateOnScreen('7.png')
# # 해당 이미지 가운데를 반환
# q = pyautogui.center(i)
# # 해당 이미지 가운데를 클릭 
# pyautogui.click(q)

# 계산기 버튼 위치값 알아와서 스크린샷 하기
# print(pyautogui.position())

# 계산기 이미지 스크린샷 하기
pyautogui.screenshot('1.png',region=(1395,643,30,30))
pyautogui.screenshot('7.png',region=(1403,542,30,30))
pyautogui.screenshot('4.png',region=(1380,585,30,30))

# 이미지 가운데 위치 알아오기
num4= pyautogui.locateCenterOnScreen('4.png')
num7= pyautogui.locateCenterOnScreen('7.png')
num1= pyautogui.locateCenterOnScreen('1.png')

pyautogui.click(num7)
pyautogui.click(num1)
pyautogui.click(num4)
pyautogui.click(num1)
pyautogui.click(num7)