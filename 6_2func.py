



# 1. 함수 정의
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# 전달값과 반환값
# 입금 함수 정의
# def deposit(balance, money):
#     print("입금이 완료되었습니다 잔액은 {} 원 입니다.".format(balance+money))
#     return balance + money

# 출금 함수 정의
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance-money))
#         return balance-money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
#         return balance

# 저녁 출금시 수수료 포함 
# def withdraw_night(balance, money):
#     commission = 100 
#     return commission, balance-money-commission # 반환값이 2개임


# 함수 사용(호출)
# balance = 0 #잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# (commission , balance) =  withdraw_night(balance, 500)
# print("수수료 {} 원이며, 잔액은 {} 원입니다.".format(commission, balance))


# 2. 함수 기본값 설정
# def profile(name, age, main_lang):
#     print("이름: {}\t나이:{}\t주 사용언어:{}\t".format(name, age, main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호", 25, "자바")

# 2.1 같은 학교 같은 학년 같은 반 같은 수업 일시....기본값 사용
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이:{1}\t주 사용언어:{2}\t".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# 3. 키워드 값 사용 함수 호출(매개변수 순서가 바뀌어도 사용 가능)
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호") 

# 4. 가변인자 사용 함수 호출
# def profile(name, age, lang1, lang2, lang3,lang4, lang5):
#      print("이름: {0}\t나이:{1}\t".format(name, age), end="")
#      print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석", 20, "Python","Java","C", "C++","C#")
# profile("김태호", 25, "Kotlin", "Swift","","","") 

# 4.1 인자를 선언한 갯수데로 넣어줘야 한다 거나, 추가되었을 때 가변인자 사용
# def profile(name, age, *language):
#     print("이름: {0}\t나이:{1}\t".format(name, age), end="")
#     for lang in language:
#         print(lang, end="")
#     print()

# profile("유재석", 20,"Python","Java","C", "C++","C#","JavaScript" )
# profile("김태호", 25, "Java","Swift")

# 5. 지역변수와 전역변수
# 5.1 함수 내에서만 사용 가능한 변수, 함수외 어디서든 사용가능한 변수

# gun = 10

# def checkpoint(solders): #경계근무
#     gun = gun-solders # 여기서 gun은 함수 내부에 있는 지역변수이다. 초기화 안되어서 오류발생
#     print("[함수 내] 남은 총 : {}".format(gun))
    

# print("전체 총 : {}".format(gun))
# checkpoint(2) # 2명이 경계근무
# print("남은 총 : {}".format(gun))

# 5.2 오류 해결
# gun = 10

# def checkpoint(solders): #경계근무
#     gun = 20
#     gun = gun-solders # gun 지역변수로  초기화 해줌
#     print("[함수 내] 남은 총 : {}".format(gun))
    

# print("전체 총 : {}".format(gun))
# checkpoint(2) # 2명이 경계근무
# print("남은 총 : {}".format(gun))

# 5.3 전역변수 예
# gun = 10

# def checkpoint(solders): #경계근무
#     global gun  #전역 공간에 있는 gun 사용
#     gun = gun-solders # gun 지역변수로  초기화 해줌
#     print("[함수 내] 남은 총 : {}".format(gun))
    

# print("전체 총 : {}".format(gun))
# checkpoint(2) # 2명이 경계근무
# print("남은 총 : {}".format(gun))

# 5.4 전역변수 사용은 권장 사항이 아님..그래서 매개변수로 전달 받고, 다시 리턴해주는 형식으로 사용함
# gun = 10

# def checkpoint_ret(gun, solders): #경계근무
#     gun = gun - solders
#     print("[함수 내] 남은 총 : {}".format(gun))
#     return gun

# print("전체 총 : {}".format(gun))
# # checkpoint(2) # 2명이 경계근무
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {}".format(gun))

# 6. 표준 입출력 함수
# print("Python","Java", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# 6.1 
# import sys
# print("Python","Java", file=sys.stdout) # 표준 출력으로 출력됨
# print("Python","Java", file=sys.stderr) # 표준 에러로 출력됨

# 6.2
# scores = {"수학" : 50, "영어":50, "코딩": 100}
# for (subject, score) in scores.items():
#     print(subject, score)

# 6.3 : 출력 줄맞추기(정형화된 포맷으로 출력) 
# scores = {"수학" : 50, "영어":50, "코딩": 100}
# for (subject, score) in scores.items():
#     print(subject.ljust(8) , str(score).rjust(4), sep=":") # 8공간 확보 하고 왼쪽 정렬, 4공간 확보 후 오른쪽 정렬

# 6.4 : 은행 대기 순번표 출력 ()
# for num in range(1,21):
#     print("대기번호 : " +str(num) ) 

# 6.4.1 : 은행 대기 순번표 출력2 (001,002....)
# for num in range(1,21):
#     print("대기번호 : " +str(num).zfill(3) ) #3공간 확보 후 빈 공간은 0으로 채우기