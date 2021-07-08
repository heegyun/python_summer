# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for wating_no in [0,1,2,3,4] : # 연속 범위일 시  range(5)
#     print("대기번호 : {}".format(wating_no))

# starbucks =["아이언맨","토르","아이엠그루트"]

# for customer in starbucks:
#     print("{} , 커피가 준비되었습니다.".format(customer))


# 스타벅스 새로운 규칙: 손님 5번 호명 하기
# customer = "토르"
# index = 5
# while index >=1 :
#     print("{}, 커피가 준비되었습니다.{}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index +=1

# customer = "토르"
# person = "Unknown" # 종업원에게 다가온 손님
# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되나요?")