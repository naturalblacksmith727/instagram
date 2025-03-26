# 주석
"""주석 입니다.
주석 입니다.
주석 입니다.
"""

# 변수
name = "홍길동"  # 문자열
age = 20  # 정수
height = 170.5  # 실수

# 변수 사용
print(name)  # 홍길동
print(age)  # 20
print(height)  # 170.5

# 여러 변수에 동식에 값을 할당
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# 여러 변수에 같은 값 할당
a = b = c = 100

print('c', c)
print('a', a)

# 올바른 변수 이름
name = 10
student_id = 1
_age = 20
Age = 30

# 앞에 숫자가 들어가서 (숫자로 시작할 수 없음)
# 2name = 20
# 하이픈(-)를 사용 불가
# my-name = 30
# 예약어 사용 불가
# if = '만약'

# 산술 연산자
a = 20
b = 10

print(a + b)  # 30
print(a - b)  # 10
print(a * b)  # 200
print(a / b)  # 2.0 (결과는 항상 실수)
print(a // b)  # 2 (결과는 정수 소수점 이하는 버림)
print(a % b)  # 0
print(a ** b)  # 10240000000000

# 비교연산자

x = 5
y = 10

print(x == y)  # False
print(x >= y)  # False
print(x <= y)  # True
print(x != y)  # True
print(x > y)  # Flase
print(x < y)  # True

age = 15
print(x < age < y)  # age가 x보다 크고 y보다 작다

# 논리 연산자

p = True
q = False

print(p and q)  # False 논리곱(AND) 둘 다 True여야 True
print(p or q)  # True 논리합(OR) 하나라도 True면 True
print(not p)  # False 논리부정(NOT) True -> False  False-> True

a = 10
b = 20
c = 30
print((a < b) and (b > c))  # False
print((a < c) or (b > c))  # True

# 할당 연산자

x = 10

x += 10
print(x)  # 20
x -= 15
print(x)  # 5
x *= 3
print(x)  # 15

# 멤버십 연산자

fruits = ["사과", "바나나", "체리"]

print("사과" in fruits)  # True
print("수박" in fruits)  # False
