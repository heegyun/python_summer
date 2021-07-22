from bs4 import BeautifulSoup

import requests

base_url = "https://search.daum.net/search?w=tot&q="
input_year = input("역대 관객 순위 확인 연도를 입력하세요 ")
plus_url= "%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

url = base_url + input_year + plus_url

# 2. html 가져오기(읽어오기)
html = requests.get(url)

# 3. 분석을 해서 
soup = BeautifulSoup(html.text, "html.parser")
# print(soup.prettify())

# 4. 분석한 것에서 원하는 것만 가져와서 결과를 출력하거나, 저장하기
# find() 함수: 하나의 컨텐츠만 찾기 
# find_all() 함수: 조건에 맞는 모든 속성을 찾기

imgs = soup.find_all("img",attrs={"class" : "thumb_img"})

n = 1

for i in imgs:
    imgUrl = i["src"]
    if imgUrl.startswith("//"):
        imgUrl = "https:" + imgUrl
    
    imgRes = requests.get(imgUrl)

    with open("./img/"+ "movie{}.jpg".format(n),"wb") as f:
            f.write(imgRes.content) # 리소스가 갖고 있는 컨텐츠 값을 파일에 쓴다.
    n+=1

    if n > 5:
        break

print("다운로드 완료")
