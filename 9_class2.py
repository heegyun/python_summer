# class Parents:
#     def __init__(self):
#         self.value= "테스트"
#         print("부모 클래스의 생성자 메소드 입니다.")
#     def test(self):
#         print("부모 클래스의 test() 메소드 입니다.")


# class Child(Parents):
#     def __init__(self):
#         Parents.__init__(self)
#         print("자식 클래스의 생성자 메소드 입니다.")


# child = Child()
# child.test()
# print(child.value)


# 1. 유닛 클래스 정의
class Unit:
    def __init__(self, name, hp, speed): # 생성자 함수: 객체를 생성할 떄 처리할 내용을 작성할 수있다.
        self.name = name # 멤버 변수
        self.hp = hp 
        self.speed =speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2} ]"\
            .format(self.name,location, self.speed))
       
  


# 2. 공격 유닛(유닛 클래스 상속)
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self,name, hp,speed)
        self.damage = damage
        
    
    
    def attack(self, location):
        print("{0} 유닛이 {1}로 공격 합니다.".format(self.name, location))

    def damaged(self, damage):
        self.hp-=damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{} 유닛이 파괴되었습니다.".format(self.name))

# 3. 공중 유닛, 공격력은 없음
class Flyable:
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도: {2}]"\
            .format(name,location,self.flying_speed))


# 4. 공중 공격 유닛: 날면서 공격할수 있는 유닛(다중 상속)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
       AttackUnit.__init__(self, name, hp, 0 ,damage)
       Flyable.__init__(self, flying_speed)
    
    # move() 오버라이딩
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리: 공중공격유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 5, 5)
valkyrie.fly(valkyrie.name,"1시")
valkyrie.move("1시")

# 벌처 유닛: 공격 유닛,  기동성이 좋다.
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력과 공격력이 좋다.
battlecuiser = FlyableAttackUnit("배틀크루저",500, 25,3)

vulture.move("11시")
battlecuiser.move("9시")

