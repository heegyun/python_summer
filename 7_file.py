# profile_file = open("basic.txt","w",encoding="utf-8")
# file.write("hello python")
# file.write("안녕하세요 파이썬이 좋아요")
# print("수학: 50", file=profile_file)
# print("영어: 100", file=profile_file)
# profile_file.close()

# 2. 파일에 내용 이어서 쓰기
# profile_file = open("basic.txt","a",encoding="utf-8")
# profile_file.write("과학:90")
# profile_file.write("\n코딩:100")
# profile_file.close()

# 3. 파일에 내용 읽기
# profile_file = open("basic.txt","r",encoding="utf-8")
# 3.1 내용을 한번에 모두 다 읽어오기
# print(profile_file.read())
# profile_file.close()

# 3.2 한줄단위로 읽어오기
# profile_file = open("basic.txt","r",encoding="utf-8")
# print(profile_file.readline(),end="")
# print(profile_file.readline(),end="")
# print(profile_file.readline(),end="")
# print(profile_file.readline(),end="")
# profile_file.close()

# 3.3 내용이 몇줄인지 알 수 없을 때 읽어 오기(반복문)
# profile_file = open("basic.txt","r",encoding="utf-8")

# while True:
#     line = profile_file.readline()
#     if not line :
#         break
#     print(line, end="")
# profile_file.close()

# 3.4 리스트에 모든 내용을 저장한 후, 출력하기
# with open("basic.txt","r",encoding="utf-8") as p:
#     lines = p.readlines() # 모든 줄에 있는 내용을 읽어와서 리스트 형태로 저장
# print(type(lines))

# for i in lines:
#     print(i, end="")


# import pickle
# 데이터 (딕셔너리, 리스트)를 파일 형태로 저장 후, 사용하게 하는 모듈
# profile_file = open("basic.pickle","wb")
# profile = {"이름" : "박명수","나이": 30, "취미": ["축구","골프","농구"]}
# print(profile)

# pickle.dump(profile,profile_file) # profile 에있는 정보를 파일에 저장.

# profile_file.close()

# profile_file = open("basic.pickle","rb")
# profile= pickle.load(profile_file)
# print(profile)
# print(type(profile))
# profile_file.close()

# 사용자로부터 입력을 받아 파일(test.txt) 에 저장하는프로그램을 작성하시오.
# 조건: 기존에 작성된 내용을 유지하고. 새로 입력한 내용을 추가해야 한다.
user_input = input("저장할 내용을 입력하세요: ")
with open("test.txt", "a", encoding="utf-8") as f:
    print(user_input,file=f)

