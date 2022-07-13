# 1. csv 파일 처리 
# with open("E:/2022년자료/Python_Summer/csv/singer1.csv", "r") as inFp:

#     inStr = inFp.readline()
#     print(inStr, end = "")

#     inStr = inFp.readline()
#     print(inStr, end = "")

# CSV는 한 줄을 모두 처리하는 것이 아니라 각 데이터를 처리해야 의미가 있음
# 즉, TWC, 트와이스, 9 … 등을 리스트에 분리해서 저장해야 이후 계산이 가능함

# 2. CSV 파일의 헤더를 별도로 먼저 읽어서 처리한 후,
# 나머지 모든 행을 리스트로 저장하고 각 항목을 분리해서 출력하는 코드

# 리스트에 내용을 탭간격으로 출력하는 함수 정의
# def printList(pList):
#     for data in pList:
#         print(data, end='\t')
#     print()

# 파일 열고, 읽기
# with open("E:/2022년자료/Python_Summer/new_singer1.csv", "r") as inFp:
#     header = inFp.readline() # 첫번째 줄 (헤더) 한줄 별도로 먼저 읽어온다.
#     header = header.strip() #  헤더 내용 중 공백을 제거 
#     header_list = header.split(',') # 헤더 내용을 구분자(,)로 구분해서 리스트에 저장
#     printList(header_list) # 함수호출(헤더 내용 먼저 출력한다.)
#     for inStr in inFp:
#         inStr = inStr.strip() # 나머지 모든 행을 리스트로 저장하고 각 항목을 분리해서 함수호출
#         row_list = inStr.split(',')
#         printList(row_list)

# 3. CSV 파일을 다른 파일로 복사하는 코드
# 단, 날짜의 형식을 “연.월.일”에서 “연/월/일”로 변경

# def printList(pList):
#     for data in pList:
#         print(data, end='\t')
#     print()

# with open("E:/2022년자료/Python_Summer/singer1.csv", "r") as inFp:
#  with open("E:/2022년자료/Python_Summer/new_singer1.csv", "w", encoding='utf8') as outFp:
#         header = inFp.readline() # 첫번째 줄(헤더) 읽어 온다.
#         header = header.strip() # 공백을 모두 제거하는 메소드
#         header_list = header.split(',') # 구분자를 기준으로 문자열을 분할해서 리스트로 저장함 예) [아이디, 이름, 인원, 주소, 국번...]
        
#         # 리스트를 문자열로 바꾸기 => 구분자.join()  # 예) mList = [아이디, 이름, 인원, 주소, 국번...] =>'#'.join(mList) =>"아이디#이름#인원#주소#국번#...." 
#         # 만약 숫자 리스트의 경우 join하기전에 모두 문자열로 변경해야함  map(함수, 리스트)로 리스트에 함수가 한번에 적용되는 방식을 사용하면 편리함
#         header_str = ','.join(map(str, header_list))

#         # 헤더부분을 문자열로 변경 후 파일에 쓰기
#         outFp.write(header_str + '\n')
#         # 나머지 행부분 
#         for inStr in inFp:
#             inStr = inStr.strip()
#             row_list = inStr.split(',')
#             printList(row_list)

#             # 리스트 맨 마지막 요소에 있는 문자열에서 일부 문자 변경하기
#             row_list[-1] = row_list[-1].replace('.', '/') # replace() : 문자열에서 일부 문자를 변경하는 함수

#             # 문자 변경후 한꺼번에 문자열로 변경하기
#             row_str = ','.join(map(str, row_list)) # join(): 문자열의 각 문자 사이에 다른 문자열 끼워 넣음
#             # 문자열 파일에 쓰기
#             outFp.write(row_str + '\n')

# print('새로운 파일 저장 성공~')