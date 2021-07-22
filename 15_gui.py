from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")
# 메뉴바 생성...
menu = Menu(root)


filename = "mynote.txt"

file_menu = Menu(menu,tearoff= 0 ) # 상위 메뉴 탭 항목 추가

# 파일 열기 (파일이 있는지 여부를 체크함)
def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as f:
           text.delete("1.0", END) # 텍스트 1라인 0번째 컬럼에서 끝까지 삭제
           text.insert(END,f.read()) # 파일 내용을 본문에 입력



def save_file():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", END)) # 1번째 라인 0번째 컬럼



file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=root.quit)

# 파일 메뉴 
menu.add_cascade(label="파일(F)", menu=file_menu)

# 편집, 서식, 보기, 도움말
menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(T)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

# 본문 내용 영역
# 스크롤 바 객체 생성
scrollbar = Scrollbar()
scrollbar.pack(side="right", fill="y") # 오른쪽에 스크롤바, 그리고 y축방향으로 채우기

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left",fill="both", expand=True)

# 스크롤 바와 텍스트 맵핑
scrollbar.config(command=text.yview)

root.config(menu=menu) # 위젯의 속성을 변경하는데 호출하는 함수


root.mainloop()