

# 공원의 입장료는 1만원이다. 만약 나이가 65세 이상이면 입장료의 20% 할인 받는다. 
# 나이는 입력을 받는다.

# age = int(input("나이는? "))
# fee = 10000
# if 65 <= age :
#     fee = int(fee * 0.8)
# else:
#     fee = 10000

# print("당신의 입장료는 {0} 원 입니다.".format(fee))


# dict_a = {}

# # 딕셔너리에 요소 추가
# dict_a["name"] = "구름"
# print(dict_a)

# del dict_a["name"]
# print(dict_a)

# 딕셔너리의 리스트를 선언
# pets=[
#     {"name" : "구름", "age" : 5},
#     {"name" : "초코", "age" : 3},
#     {"name" : "아지", "age" : 1},
#     {"name" : "호랑이", "age" : 1}
#    ]

# print("# 우리 동네 애완 동물들")

# 실행결과
# 우리 동네 애완 동물들
# 구름 5살
# 초코 3살
# 아지 1살
# 호랑이 1살

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1


print(counter)

