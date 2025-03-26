from sys import getsizeof
# 데이터 타입(Data Type)
# 1. 숫자

# 정수(integer) - 소수점이 없는 숫자
a = 10

# 실수(float) - 소수점이 있는 숫자
b = 3.14

# 복소수(Complex) = 실수부와 허수부로 구성된 숫자
c = 3 + 4j

print(a, type(a))
print(b, type(b))
print(c, type(c))

# 2. 문자열(string)
name = "에단"
print(name, type(name))

# 3. 불리언(Boolean)
참 = True
거짓 = False

print(참, type(참))
print(거짓, type(거짓))

# 비교 연산의 결과로 불리언 값을 얻을 수 있습니다.
print('bool', 10 > 5, type(10 > 5))
print('bool', 10 == 5, type(10 == 5))
print('bool', 10 <= 5, type(10 <= 5))

# None 타입
# 아직 값이 할당되지 않았음을 표시
result = None

str = '문자열입니다.'
print(getsizeof(1))
print(getsizeof("문자열"))
print(getsizeof(str))

# num = input("숫자입력 하세요 :")
# print(num, type(num))
# a = int(num) / 2
# print(a)  # 15.0

x = 3

print(int(x))  # 3


# 이스케이프 문자
print("안녕\n하세요")
print("안녕\t하세요")
print("안녕\'하세요")
print("안녕\"하세요")
print("안녕\\하세요")

# 문자열 포맷팅
year = ("올해는 %d년 %s의 해이다" % (2024, "용띠"))
print(year)

number = "저는 올해 %d살 입니다." % 20
print(number)

clac = "10 나누기 3는 %.3f입니다." % 3.33333
print(clac)

text = "저는%5s에서 살고 있습니다." % "은평구"
print(text)


# 문자열 포맷팅 2
country = "대한민국"
city = "서울"
people = "한국인"
text = "저는 올해 {0}살입니다.".format(20)
print(text)

text = "저는 올해 {age}살입니다.".format(age=20)
print(text)

text = "저는 올해 {0}살입니다. 나는 {1}에서 살고 있습니다. 나는 {2}입니다.".format(
    20, "은평구", "한국인")
print(text)

text = "나는 {country}에서 살고 있습니다. 나는 {city}에서 살고 있습니다. 나는 {people}입니다.".format(
    country=country, city=city, people=people)
print(text)

text = "나는 {1} {2}에서 살고 있습니다. 나는 {0}입니다.".format(
    "한국인", "대한민국", "서울")
print(text)

text = "{} {{점수는:}} {}점".format("수학", 95)
print(text)
text = "{} 점수: {}점".format("수학", 95)
print(text)


text = "[{0:$<10}]".format("hey")
print(text)


country = "대한민국"
city = "서울"
people = "한국인"

text = f"나는 {country}에서 살고 있습니다. 나는 {city}에서 살고 있습니다. 나는 {people}입니다."
print(text)


# 실습
print("|\_/|")
print("|q p|")
print('( 0 )"""\\')
print('|"^"`   |')
print('||_/=\\\\__|')

print("|\_/|\n|q p|\n( 0 )\"\"\"\\\n|\" ^ \"`  |\n||_/=\\\\__|\n")

# 실습2
name = "에단"
text = f"{name:=^10}"
print(text)

print(f"문자열 실습입니다. {{ 중괄호 }}를 출력해보세요")


# 문자열 인덱싱
print()
print("문자열 인덱싱")
print()

a = "Hello, Python"

print("a[7]", a[7])
print("a[-6]", a[-6])

print(a[7] + a[8] + a[9] + a[10] + a[11] + a[12])
print(a[-6] + a[-5] + a[-4] + a[-3] + a[-2] + a[-1])

print("a[0:5]", a[0:5])
print("a[7:]", a[7:])
print("a[:5]", a[:5])
print("a[:]", a[:])

date = "20240930"
print(date[:4] + "년" + date[4:6] + "월" + date[6:] + "일")

print(len(date))
print(date.count('2'))

print(date.find('5'))
# print(date.index('5'))

# replace 첫번째 변경하고자 하는 문자, 두번째 변경할 문자, 갯수
print(date.replace('0', '1', 2))

# split(나누고 싶은 문자)
print(date.split('0'))

text = "Hello, Python"
print(text.upper())
print(text.lower())

text = "           Hello    World          "
print("[" + text.strip() + "]")
print("[" + text.lstrip() + "]")
print("[" + text.rstrip() + "]")

# 숫자 판별
print("123".isdigit())

# 문자, 공백 판별
print("hello".isalpha())
print("hello123".isalnum())
print('\n\t'.isspace())

text = "Hello"
print(text.upper().isupper())
print(text.lower().islower())

print(text.istitle())


# 실습
# 입출력 실습 - 다음과 같이 실행되도록 코드를 작성하세요.

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))

print(f"안녕하세요. {name}님! 당신의 나이는 {age}살입니다.")


# 실습2
# 입출력 실습 - 다음과 같이 실행되도록 코드를 작성하세요.

name = input("이름을 입력하세요: ")
year = int(input("태어난 년도를 입력하세요: "))
now = int(input("현재 년도를 입력하세요: "))

print(f"안녕하세요. {name}님! 당신은 {now - year + 1}살입니다.")
