# Quiz) 사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 → naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 → naver
# 규칙3 : 남은 글자 중 처음 세 자리 + 글자 갯수 + 글자 내 'e'의 갯수 + '!'로 구성
#                        (nav)                      (5)                   (1)             (!)

# 예) 생성된 비밀번호 : nav51!

#url = "http://naver.com"
url = "http://daum.net"
# url = "http://google.com"
# url = "http://youtube.com"

my_str = url.replace("http://", "") # 규칙 1

my_str = my_str[:my_str.index(".")] # 규칙 2
# naver.com 일 때 my_str.index(".") 의 결과는 5 이므로 위 문장은
# my_str = mystr[0:5] 와 같음

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙 3

print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))