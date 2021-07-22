import numpy as np

# 1. 0부터 5까지를 가지고 1차원 벡터 배열을 생성
# a = np.arange(6)
# print(a)

# 2. reshape()함수 사용 하여 2차원 형태의 3행 2열 행렬 만들기 
# a = a.reshape(3,2) 
# print(a)

# 3. 3차원 형태의 다차원 배열을  생성
# a = np.arange(8)
# a = a.reshape(2,2,2)

# 4. 2차원 형태의 3x2 행렬을 나타내고, a = a+10과 같이 행렬 각각 원소에 10을 더하는
# 연산을 반복문 없이 간단히 프로그래밍 할수 있는 장점이 있음
# a = np.arange(6)
# a = a.reshape(3,2)
# print("**덧셈 연산 전의 행렬값**")
# print(a)

# a = a+10
# print("\n**덧셈 연산 후의 행렬값**")
# print(a)

# pandas: 데이터를 수집하고 분석하는데사용되는 라이브러리
# Series : 1차원  배열 형태, DataFrame : 2차원 배열 형태 객체 

import pandas as pd
# dict1 = {'A':'hello', 'B':2, 'C': 4.5, 'D':'AB', 'E':True}

# sr1 = pd.Series(dict1)
# print(sr1)

dict1 = {'A':[1,2,3], 'B':[4,5,6], 'C': [6,7,8], 'D':[9,10,11]}
df1 = pd.DataFrame(dict1)
print(df1)




# from tkinter.font import Font
# import matplotlib.pyplot as plt
# import random
# from matplotlib import font_manager, rc


# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)

# plt.title("산포도 그래프")

# for i in range(100):
#     x = random.uniform(0.0, 6.0)
#     y = random.uniform(0.0, 100.0)
#     plt.scatter(x, y, s=10)

# plt.ylabel("y축 값: ")
# plt.xlabel("x축 값: ")

# plt.show()