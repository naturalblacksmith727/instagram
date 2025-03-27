""" 조건문
    1. if 조건식:
        조건식이 참이라면 실행
"""

# 1. if 조건식:
if True:
    print('참 입니다.')

# 2. if 조건식:
if False:
    print('거짓 입니다.')

""" 조건문 예제 """
age = 15

if age > 16:
    print('15살 이상입니다.')

#  조건문과 상관없이 실행
print('끝!')

# 3. if 조건식:

if []:
    print("리스트가 비어 있습니다.")

if [1, 2, 3]:
    print("리스트가 비어 있지 않습니다.")

if "":
    print("문자열이 비어 있습니다.")

if "Hello":
    print("문자열이 비어 있지 않습니다.")

if {}:
    print("딕셔너리가 비어 있습니다.")

if {"key": "value"}:
    print("딕셔너리가 비어 있지 않습니다.")

if ():
    print("튜플이 비어 있습니다.")

if (1, 2, 3):
    print("튜플이 비어 있지 않습니다.")

if set():
    print("세트가 비어 있습니다.")

if {1, 2, 3}:
    print("세트가 비어 있지 않습니다.")

if None:
    print("None 입니다.")

if 10:
    print("숫자가 10 입니다.")

if 0:
    print("숫자가 0 입니다.")

# 실습 1
pw = input("비밀번호를 입력하세요: ")

if pw == "abc123":
    print("비밀번호가 일치합니다.")

# 실습 2
num = int(input("숫자를 입력하세요: "))

if num % 2 == 0:
    print("짝수입니다.")
