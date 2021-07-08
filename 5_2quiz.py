# 당신은 Cocoa 서비스를 이용하는 택시 기사님 입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

#(출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 :  2 분



# from random import *
# cnt = 0 # 총 탑승 승객 수

# for i in range(1, 51) : # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요시간

#     if 5<= time <=15: # 5분 ~ 15분 이내 손님(매칭 성공), 탑승 승객 수 증가 처리
#         print("[O] {0} 번째 손님 (소요시간 :  {1}분)".format(i , time))
#         cnt +=1
#     else: # 매칭 실패한 경우
#          print("[ ] {0} 번째 손님 (소요시간 :  {1}분)".format(i , time))

# print("총 탑승 승객 :  {} 분".format(cnt))


# 숫자 맞추기 게임 
# 1부터 30까지의 임의의 난수 를 생성해서 입력한 숫자와 비교하여 몇회에 숫자를 맞추는지 확인하는 
# 프로그램을 작성하시오.

import random
guessNumber = random.randint(1,31)

playNumber = -1 

count = 1 
limit = 5 # 제한 횟수 5로 초기화

playAgain = "YES" # 게임 반복 상태 설정

while playAgain == "YES":
    while count <= limit and guessNumber != playNumber :
        playNumber = int(input("숫자를 입력하세요>>"))
        if guessNumber  ==  playNumber:
            break
        elif guessNumber < playNumber:
            print("입력한 숫자가 컴퓨터가 가지고 있는 숫자 보다 커요!")
        else:
            print("입력한 숫자가 컴퓨터가 가지고 있는 숫자 보다 작아요!")
        count+=1

    if guessNumber == playNumber:
        print("{}번만에 맞혔어요 !! 축하합니다.".format(count))
        if limit >1:
            limit -= 1
    else:
        print("컴퓨터가 가진 수는: {}  입니다.".format(guessNumber)) 
        limit+=1  

    playAgain = input("게임을 다시 시작할까요? YES or NO")
    count=1
    guessNumber = -1


