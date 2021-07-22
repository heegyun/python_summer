from os import read
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# 1. url 부분 
baseurl = "https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query="
pluseurl = input("검색어를 입력하세요: ")
url = baseurl + quote_plus(pluseurl)
#https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EC%82%AC%EA%B3%BC
#print(url)

# 2. html 가져오기(읽어오기)
html = urlopen(url).read()

# 3. 분석을 해서 분석한 것에서
soup = BeautifulSoup(html, "html.parser")
print(soup)

# 4. 원하는 것만 가져와서 결과를 출력하거나, 저장하기

# find() 함수: 하나의 컨텐츠만 찾기 
# find_all() 함수: 조건에 맞는 모든 속성을 찾기
img = soup.find_all(class_='_image _listImage') 

n = 1
for i in img:
    imgurl = i['data-source'] # 이미지 리소스 주소
    with urlopen(imgurl) as f: # 이미지 리소스를 열어서
        with open('./img/'+ pluseurl + str(n) + 'jpg', 'wb') as uf: # 사과1.jpg, 사과2.jpg, 포도.
            img = f.read()
            uf.write(img)
    n += 1
    print(imgurl)

print("다운로드 완료")
 

