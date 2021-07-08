# 퀴즈2
# 변수를 이용하여 다음 문장을 출력하시오.
# 변수명: station, 변수값:"용운동","가양동","자양동" 순서대로 입력
# 출력 문장:  xx행 버스가 들어오고 있습니다.

station = "자양동"
print( "{} 행 버스가 들어오고 있습니다.".format(station))




# 퀴즈3
# 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다. 
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 단, 조건1: 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되, 중복 불가
# 조건3: random 모듈의 shuffle과 sample 을 활용

# 출력 예제:
# -- 당첨자 발표 --
# 치킨 당첨자 :  1
# 커피 당첨자 : [2,3,4]
# -- 축하합니다. --

# 활용 예제
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,2))






# 퀴즈1

# station = "용운동"
# print(station+"행 버스가 들어오고 있습니다.")

# # 퀴즈2
from random import *

users = range(1,21)

# print(type(users))
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : : {}".format(winners[1:]))
print("-- 축하합니다. --")