# import matplotlib.pyplot as plt
# from matplotlib import font_manager,rc


# 1. 선그래프 그리기
# plt.plot([1,2,3,4]) # plot(x축값, y축값, 옵션) 
# plt.ylabel("y-axis values") #y축 이름 표시
# plt.show()

# 2. 점 그래프 그리기
# plt.plot([1,2,3,4], [1,7,5,10], "ro") # plot(x축값, y축값, 옵션) ro: red,circle(색과마커모양) 
# plt.axis([0,6,0,12]) # x축값의 범위와 y축값의 범위를 지정한다.
# #plt.ylabel("y-axis values") #y축 이름 표시
# plt.show()

# 3.막대 그래프 그리기
# plt.bar([1,2,3,4], [1,7,5,10])  
# plt.axis([0,6,0,12]) # x축값의 범위와 y축값의 범위를 지정한다.
# plt.show()

# 4. 여러 개 그래프  한번에 보여주기
# 한글 폰트 지정: window/fonts/ 폰트 가져오기
# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
# rc("font",family=font_name)

# plt.figure(figsize=(10,10)) # 그래프 가로, 세로 크기

# plt.subplot(2,1,1)
# plt.title("점그래프")
# plt.plot([1,2,3,4,5],[1,7,5,10,11],"ro")
# plt.axis([0,6, 0,12])

# plt.subplot(2,1,2)
# plt.title("막대 그래프")
# plt.bar([1,2,3,4,5],[1,7,5,10,11])
# plt.axis([0,6, 0,12])
# plt.show()

# 5. 산포도 그래프 그리기
import random
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc

font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
rc("font",family=font_name)

plt.title("산포도 그래프")

for i in range(100):
    x = random.uniform(0.0, 6.0)
    y = random.uniform(0.0, 100.0)
    plt.scatter(x, y, s=10) # scatter() : 많은 점을 원하는 크기로 나타내기, 크기가 10인 원모양으로 산포도 표현


plt.xlabel("x축 값")
plt.ylabel("y축 값")
plt.show()

