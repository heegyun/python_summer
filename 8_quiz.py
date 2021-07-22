# 퀴즈1 : 성적 처리 프로그램 
# 학생의 성적을 처리하고자 한다, 학생의 성적은 중간, 기말, 과제에 의해결정된다.
# 학생별로, 학생 이름, 중간고사, 기말고사, 과제 성적을 입력받아 학생이 얻은 점수의 
# 합과 평균을 구해서 알려주는 프로그램을 작성하시오.

# 입력:학생이름을 문자열로 입력, 중간, 기말, 과제성적을 정수형으로 입력 
# 출력: 학생이름, 계산된 합계, 계산된 평균

# 출력 형식
# 학생이름 = 홍길동
# 합계 = 210
# 평균 = 70.0


#  
# 학생 클래스 정의
# 생성자: 멤버변수 초기화 
# 메소드1: get_name(self): 학생이름을 반환한다. 
# 메도스2: get_sum(self): 합계를 반환한다. 
# 메소드3: get_avg(self):평균을 반환
# 메소드4: calculator(self) :합과 평균을 계산하는 메소드 








class Student:
    def __init__(self, name, midscore, finalscore, report) :
        self.name = name
        self.midscore = midscore
        self.finalscore = finalscore
        self.report = report

    def get_name(self): # self.name 직접 접근 가능
        return self.name
    
    def get_sum(self):
        return self.sum
    
    def get_avg(self):
        return self.avg

    def calculator(self):
        self.sum = self.midscore+self.finalscore+self.report
        self.avg = round(self.sum / 3, 2)

name = input("이름 입력:  ")
midscore = int(input("중간 고사 성적 입력: "))
finalscore = int(input("기말 고사 성적 입력: "))
report = int(input("과제 성적 입력: "))

student1 = Student(name, midscore, finalscore, report)
student1.calculator()
print("학생이름 = ", student1.get_name())
print("합계 = ", student1.get_sum()) 
print("평균 = ", student1.get_avg())
