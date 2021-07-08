# 이름, 나이, 전화번호 를 입력 받아오는 프로그램을 작성해보시오.
# 이름은 name 변수,  나이는 age, 전화번호는 tel 변수에 저장하도록 하시오.
# name = input("이름을 입력해 주세요> ")
# age = input("나이를 입력해 주세요> ")
# tel = input("전화번호를 입력해 주세요> ")
# print("당신의 이름은 " , name, "나이는 " , age, "전화번호는", tel," 입니다" )
# print(type(age))

# 숫자를 입력 받고 덧셈하기
# num = int(input("숫자를 입력하세요 "))
# print(num + 100)

# print(int("안녕하세요"))
# print(float("안녕하세요"))
# print(int("52.273"))

# a = [1,2,3]
# print(id(a))

# b = a
# print(id(b))

# print(a is b)

# [a,b] = ['python','life']
# print(a,b)

# a = b = 'python'
# print(a,b)

# a =  5
# b = 3
# print(a)
# print(b)
# a,b = b,a
# print(a)
# print(b)

# 문자열 입력> 안녕하세요
# 문자열 입력> 반갑습니다.
# 출력1: 안녕하세요 반갑습니다.
# 출력2: 반갑습니다 안녕하세요

a = input("문자열 입력>")
b = input("문자열 입력>")

print(a,b)

a,b = b,a
# temp = a
# a = b
# b = temp

print(a,b)