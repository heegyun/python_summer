# 종족간 싸움: 스타크래프트
# 마린: 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력{} \n ".format(hp, damage))

# # 탱크: 공격 유닛, 탱크, 포를 쏠 수 있다. 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력{} \n ".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {}, 공격력{} \n ".format(tank2_hp, tank2_damage))

# # 공격 함수 정의
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력:{2} ".format(\
#         name, location, damage))


# 유닛이 더 많이 필요할 시, 매번 2,3,4,이런식으로 거의 유사 코드를 계속 반복해서 만들어야 할 때
# 클래스를 사용하여 쉽게 문제를 해결할 수 있다.

# 1. 유닛 클래스 정의
# class Unit:
#     def __init__(self, name, hp, damage): # 생성자 함수: 객체를 생성할 떄 처리할 내용을 작성할 수있다.
#         self.name = name # 멤버 변수
#         self.hp = hp 
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {}, 공격력{} \n ".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스",80,5)
# print("유닛이름: {0}, 공격력:{1}".format(wraith1.name,wraith1.damage))

# wraith2 = Unit("레이스2", 80,5)
# wraith2.clocking = True

# if wraith1.clocking == True:
#     print("{} 는 현재 클로킹 상태 입니다.".format(wraith1.name))


# 공격 유닛 클래스를 정의하시오.
# 클래스 이름: AttackUnit
# 메소드 : attack(self, location), damaged(self, damage): hp가 0이하이면 유닛은 파괴되었습니다.출력

# 파이어벳: 공격 유닛, 화염방사기,hp:50, damage: 16
# attack("5시")
# damaged(25)
# damaged(25)

# 2. 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력{} \n ".format(self.hp, self.damage))
    
    
    def attack(self, location):
        print("{0} 유닛이 {1}로 공격 합니다.".format(self.name, location))

    def damaged(self, damage):
        self.hp-=damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{} 유닛이 파괴되었습니다.".format(self.name))

firebat = AttackUnit("파이어뱃",50,16)
firebat.attack("1시")
firebat.damaged(25)
firebat.damaged(25)

