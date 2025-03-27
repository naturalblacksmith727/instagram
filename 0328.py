""" 조건문
    1. if 조건식:
        조건식이 참이라면 실행
"""

# 1. if 조건식:
if True:
    print('참 입니다.')
else:
    print('거짓 입니다.')

# 2. if 조건식:
if False:
    print('참 입니다.')
else:
    print('거짓 입니다.')

""" 조건문 예제 """
age = 15

if age >= 20:
    print('20살 이상입니다.')
else:
    print('미성년자입니다.')

#  조건문과 상관없이 실행
print(f'나이는 {age} 입니다.')

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
# pw = input("비밀번호를 입력하세요: ")

# if pw == "abc123":
#     print("비밀번호가 일치합니다.")
# else:
#     print('비밀번호가 틀렸습니다.')

# # 실습 2
# num = int(input("숫자를 입력하세요: "))

# if num % 2 == 0:
#     print("짝수입니다.")
# else:
#     print('홀수 입니다.')


""" 조건문 예제 """
age = int(input("입력해주세요"))

if age >= 40:
    print('40대 입니다.')
elif age >= 30:
    print('30대 입니다.')
elif age >= 20:
    print('20대 입니다.')
else:
    print('미성년자입니다.')

""" 실습 3 """
score = input("성적을 입력해주세요")

if score.isdigit():
    score = int(score)
    if score >= 90:
        print('학점: A')
    elif score >= 80:
        print('학점: B')
    elif score >= 70:
        print('학점: C')
    elif score >= 60:
        print('학점: D')
    else:
        print('학점: F')
else:
    print('숫자를 입력해주세요')


age = int(input("나이를 입력해주세요"))
# 결제 방식
payment = input("결제 방식을 입력해주세요")

if age >= 75:
    print(f'{age}세 요금은 무료 입니다.')
elif 20 <= age < 75:
    if payment == '카드':
        print(f'{age}세 카드 요금은 1200원 입니다.')
    else:
        print(f'{age}세 현금 요금은 1300원 입니다.')
elif 14 <= age < 20:
    if payment == '카드':
        print(f'{age}세 카드 요금은 720원 입니다.')
    else:
        print(f'{age}세 현금 요금은 1000원 입니다.')
elif 8 <= age < 14:
    print(f'{age}세 요금은 450원 입니다.')
else:
    print(f'{age}세 요금은 무료 입니다.')


print()
print()
print()
