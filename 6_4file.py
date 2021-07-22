# 파일에 내용 덮어쓰기 (옵션:w)
# score_file = open("score.txt","w",encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# 파일에 내용 이어서 쓰기 (옵션:a(ppend))
# score_file = open("score.txt","a",encoding="utf-8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# # 파일 내용 읽기
# score_file = open("score.txt","r", encoding="utf-8")
# 1. 한번에 모두 읽기
# print(score_file.read())
# score_file.close()

# 2. 한줄 단위로 읽어오기
# score_file = open("score.txt","r", encoding="utf-8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# 3. 파일을 읽어오는 내용이 몇줄인지 모를 때(반복문 사용)
# score_file = open("score.txt","r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# # 4. 리스트에 모든 내용을 저장한 후 출력하기
# score_file = open("score.txt","r", encoding="utf-8")
# lines = score_file.readlines() # 모든 줄에 있는 내용읽어와서 list 형태로 저장
# for line in lines:
#     print(line, end="")


# pickle 모듈 사용
# 프로그램에서 사용하는 
# 1. 데이터(리스트,딕셔너리,등)를 파일형태로 저장 후, 다시 pickle을 사용하여 열고 사용
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile ={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()


# 2. 데이터를  다시 pickle을 사용하여 열고 사용
import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 pickle로 열어 사용
print(profile)
