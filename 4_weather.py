# 조건문 퀴즈1
# "오늘 날씨 어때?" 라고 묻고 사용자로부터 날씨(weather)를 입력받는다.
# 날씨(weather)가  비가 오거나 눈이오면 우산을 챙기세요 
# 날씨(weather)가  미세머지 이면 마스크를 챙기세요
# 날씨(weather)가 맑음이면 준비물 필요 없어요


# 조건문 퀴즈2
# "오늘 기온 어때?" 라고 묻고 사용자로부터 기온(temp)을 입력받는다.
# 기온(temp)이  30도 이상이면 많이 더워요 나가지 마세요
# 기온(temp)이 10도 이상 30도 미만이면 괜챦은 날씨입니다.
# 기온(temp)이 0도 이상 이고 10도 미만이면 외투를 챙기세요
# 기온(temp)이 0도 이하이면 추워요 나가지 마세요










# weather = "비"
# if weather == "비" :
#     print("우산을 챙기세요")

# weather = "미세먼지"
# if weather == "비" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")

# weather = "맑아요"
# if weather == "비" :
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")


# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜챦은 날씨예여")
elif 0 <=  temp  < 10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")