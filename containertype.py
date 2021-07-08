
list_a = [273,32,103,"문자열",True,False]
#print(list_a)
#print(type(list_a))
#print(list_a[0])
#print(list_a[:3])

# 중첩된 리스트에서 슬라이싱
#a=[1,2,3,['a','b','c'],4,5]
#print(a[2:5])
#print(a[3])
#print(a[3][:2])

# b = ['a','c','b']
#b.sort()
#print(b)
# b.reverse()
# print(b)

# 중첩 튜플
# t1=('a','b',('ab','cd'))
# print(t1)
# print(t1[2])

# 퀴즈
#1. 홍길동씨의 주민등록번호는 881120-1068234 이다. 홍길동씨의 주민등록 번호를
# 연월일 (yyyymmdd) 부분과 그 뒤의 숫자 부분으로 나누어 출력하시오.

#2. [1,3,5,4,2] 리스트를 [5,4,3,2,1] 로 만들어 보시오.

#3. ['Life','is','too','short'] 리스트를 Life is too short 로 만들어 출력해 보시오.
a = ['Life','is','too','short']
b = " ".join(a)
print(b)


#4. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보시오.
# a = 1,2,3
# a = a + (4,)
# print(a)



#5. 딕셔너리 a 에서 'B'에 해당되는 값을 추출해보시오.
# a ={'A':90,'B':80, 'C':70}

#6. a 리스트에서 중복 숫자를 제거해 보시오.
c = [1,1,1,2,2,3,3,3,4,4,5]
# Cset = set(c)
# Dlist = list(Cset)
# print(Dlist)
# remove()는 값만 전달해서 제거할 수 있다.
# 인덱스를 전달해서 제거할 때는 pop() 을 이용한다.
c.pop(0)
c.pop(1)
c.pop(2)
c.pop(3) #[1,2,3,3,4,4,5]
c.pop(3) #[1, 2, 3, 4, 4, 5]
c.pop(4) #[1, 2, 3, 4, 5]

print(c)










