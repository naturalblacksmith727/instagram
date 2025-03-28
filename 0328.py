# """ 조건문
#     1. if 조건식:
#         조건식이 참이라면 실행
# """

# # 1. if 조건식:

# if True:
#     print('참 입니다.')
# else:
#     print('거짓 입니다.')

# # 2. if 조건식:
# if False:
#     print('참 입니다.')
# else:
#     print('거짓 입니다.')

# """ 조건문 예제 """
# age = 15

# if age >= 20:
#     print('20살 이상입니다.')
# else:
#     print('미성년자입니다.')

# #  조건문과 상관없이 실행
# print(f'나이는 {age} 입니다.')

# # 3. if 조건식:

# if []:
#     print("리스트가 비어 있습니다.")

# if [1, 2, 3]:
#     print("리스트가 비어 있지 않습니다.")

# if "":
#     print("문자열이 비어 있습니다.")

# if "Hello":
#     print("문자열이 비어 있지 않습니다.")

# if {}:
#     print("딕셔너리가 비어 있습니다.")

# if {"key": "value"}:
#     print("딕셔너리가 비어 있지 않습니다.")

# if ():
#     print("튜플이 비어 있습니다.")

# if (1, 2, 3):
#     print("튜플이 비어 있지 않습니다.")

# if set():
#     print("세트가 비어 있습니다.")

# if {1, 2, 3}:
#     print("세트가 비어 있지 않습니다.")

# if None:
#     print("None 입니다.")

# if 10:
#     print("숫자가 10 입니다.")

# if 0:
#     print("숫자가 0 입니다.")

# # 실습 1
# pw = input("비밀번호를 입력하세요: ")

# if pw == "abc123":
#     print("비밀번호가 일치합니다.")
# else:
#     print('비밀번호가 틀렸습니다.')

# # # 실습 2
# num = int(input("숫자를 입력하세요: "))

# if num % 2 == 0:
#     print("짝수입니다.")
# else:
#     print('홀수 입니다.')


# """ 조건문 예제 """
# age = int(input("입력해주세요"))

# if age >= 40:
#     print('40대 입니다.')
# elif age >= 30:
#     print('30대 입니다.')
# elif age >= 20:
#     print('20대 입니다.')
# else:
#     print('미성년자입니다.')

# """ 실습 3 """
# score = input("성적을 입력해주세요")

# if score.isdigit():
#     score = int(score)
#     if score >= 90:
#         print('학점: A')
#     elif score >= 80:
#         print('학점: B')
#     elif score >= 70:
#         print('학점: C')
#     elif score >= 60:
#         print('학점: D')
#     else:
#         print('학점: F')
# else:
#     print('숫자를 입력해주세요')


# age = int(input("나이를 입력해주세요"))
# # 결제 방식
# payment = input("결제 방식을 입력해주세요")

# if age >= 75:
#     print(f'{age}세 요금은 무료 입니다.')
# elif 20 <= age < 75:
#     if payment == '카드':
#         print(f'{age}세 카드 요금은 1200원 입니다.')
#     else:
#         print(f'{age}세 현금 요금은 1300원 입니다.')
# elif 14 <= age < 20:
#     if payment == '카드':
#         print(f'{age}세 카드 요금은 720원 입니다.')
#     else:
#         print(f'{age}세 현금 요금은 1000원 입니다.')
# elif 8 <= age < 14:
#     print(f'{age}세 요금은 450원 입니다.')
# else:
#     print(f'{age}세 요금은 무료 입니다.')


# # 삼항연산자
# age = int(input("나이를 입력하세요: "))
# message = "성인 입니다." if age >= 20 else "미성년자 입니다."
# print(message)

# # pass 키워드
# if age > 20:
#     pass
# else:
#     print(message)


# # 시퀀스 in 연산자
# fruit = input("과일을 한글로 입력하세요: ")

# if fruit in ['사과', '바나나', '복숭아']:
#     print('이 과일은 포함되어 있습니다.')
# else:
#     print('존재하지 않는 과일 입니다.')


# # 시퀀스 in 연산자
# fruits_calroies = {'apple': 95, 'banana': 105, 'cherry': 50}
# fruit = input("과일을 영문으로 입력하세요: ")

# # 딕셔너리에 키가 존재하는지 확인
# if fruit in fruits_calroies:
#     print(f"{fruit}의 칼로리는 {fruits_calroies[fruit]} Kcal 입니다.")
# else:
#     print(f"존재하지 않는 과일")


# '''
# 반복문
# 1. while 조건식:
#     조건식이 참이라면 실행
# '''

# # 1부터 10까지의 합
# i = 1
# total = 0
# while i <= 10:
#     total += i
#     i += 1
# # 결과 출력
# print(f'1부터 10까지의 합은 {total}입니다')


# # 문자열 입력받기
# user_input = ""
# # 문자열이 종료가 아니라면 반복
# while user_input != "종료":
#     # 문자열 입력
#     user_input = input("종료하려면 '종료'를 입력하세요:")
#     # 결과 출력
#     print(f'입력한 값: {user_input} 입니다.')


# # 무한 반복
# i = 0
# while True:
#     # 종료 조건
#     if i == 10000:
#         break
#     # 짝수 입니다.
#     if i % 2 == 0:
#         print('짝수 입니다.')
#         continue
#     # 홀수 입니다.
#     print(f'i는 {i} 입니다.')
#     # i += 1

# print('종료')


# # continue 키워드
# while True:
#     user_input = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료) :")

#     # 종료 조건
#     if user_input == "종료":
#         break

#     # 숫자 입력 조건
#     if not user_input.isdigit():
#         print("양수만 입력하세요.")
#         # 다시 입력받기
#         continue

#     # 입력된 숫자를 정수로 변환
#     number = int(user_input)

#     # 0 입력 조건
#     if number == 0:
#         # 다시 입력받기
#         continue

#     # 1부터 n까지의 합 계산
#     i = 1
#     # 합계 초기화
#     total = 0
#     while i <= number:
#         total += i
#         i += 1
#     # 결과 출력
#     print(f'1부터 {number}까지의 합은 {total} 입니다.')


# # for 반복문
# for i in range(1, 10):
#     print(i)

# # 리스트 반복
# fruits = ['사과', '바나나', '체리']

# # 리스트 반복
# for fruit in fruits:
#     print(fruit, end=' ')

# print()

# # 범위 반복
# numbers = [1, 2, 3, 4, 5]

# # 합계 초기화
# total = 0

# # 리스트 반복
# for num in numbers:
#     total += num

# # 결과 출력
# print(f'합계는 {total} 입니다.')

# # 범위 반복
# for num in range(1, 12, 2):
#     if num > 5:
#         print(num, end=' ')
# print()

# # 딕셔너리 반복
# dict1 = {'name': '홍길동', 'age': 25, 'city': '서울', 'hobby': ['캠핑', '등산']}

# # 딕셔너리 반복
# for key in dict1:
#     print(key, end=' ')
# print()

# # 딕셔너리 반복
# for value in dict1.values():
#     print(value, end=' ')
# print()

# # 딕셔너리 반복
# for key in dict1.keys():
#     print(f'{key} : {dict1[key]}', end=' ')
# print()

# # 딕셔너리 반복
# for key, value in dict1.items():
#     print(f'{key} : {value}', end=' ')

# print()

# # 구구단
# num = int(input('몇단을 출력할까요? '))

# # 구구단 반복
# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')

# # 반복문 실습 1
# num = int(input('어디까지 계산할까요?: '))

# # 합계 초기화
# total = 0

# # 1부터 num까지의 홀수만 더하기
# for i in range(1, num + 1):
#     # 홀수 조건
#     if i % 2 != 0:
#         total += i

# # 결과 출력
# print(f'1부터 {num}까지의 홀수의 합: {total}')

# # 반복문 실습 2
# students = {
#     "학생1": {'국어': 83, '영어': 92, '수학': 88},
#     "학생2": {'국어': 90, '영어': 79, '수학': 86},
#     "학생3": {'국어': 88, '영어': 86, '수학': 94},
# }


# # 학생 반복
# for key, vaule in students.items():
#     # 합계 계산
#     total = sum(vaule.values())
#     # 평균 계산
#     avg_score = total / len(vaule)
#     # 결과 출력
#     print(f'{key}의 평균 점수: {avg_score:.2f}')


# # 이중 반복문
# for i in range(1, 3):
#     for j in range(4, 7):
#         print(f' {i}, {j} ')

# # 이중 반복문
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # 합계 초기화
# total = 0

# # 이중 반복문
# for row in matrix:
#     for element in row:
#         total += element

# # 결과 출력
# print('total :', total)

# # 이중 반복문
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(matrix[i][j])

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '이프로']

while True:
    print('남은 음료수', vending_machine)

    user_input = input('사용자 종류를 입력하세요: \n1.소비자 \n2.주인\n3.종료\n')

    # 소비자
    # 조건 1.
    # 사용자는 소비자, 주인 두가지 종류로 입력받기 (번호 또는 값 입력), 그 외의 값은 잘못된 값으로 출력

    # 조건 2.
    # 소비자일 때 마시고 싶은 음료를 입력받기
    if user_input == '1':
        vending = input('마시고 싶은 음료? ')

        if vending in vending_machine:
            vending_machine.remove(vending)
        # 조건 2-1.
        # 값이 있으면 vending_machine에서 제거, 없으면 없음 출력
        else:
            print(f'{vending}가 없습니다.')
    # 주인
    # 조건 3.
    # 주인일 떄 추가, 삭제 두가지 종류 이벽 받기 (조건1과 같게)
    elif user_input == '2':
        input1 = input('할 일 선택\n1.추가\n2.삭제\n')
        if input1 == '1':
            # 추가
            # 조건 3-1.
            # 추가할 때 음료수 입력받고 vending_machine에 추가, 같은 값끼리 연결되게 출력

            add_input = input('추가할 음료수\n')
            vending_machine.append(add_input)
            vending_machine.sort()
            print('추가 완료')
        elif input1 == '2':
            # 삭제
            del_input = input('삭제 할 음료수\n')
            if del_input in vending_machine:
                vending_machine.remove(del_input)
            # 조건 3-2.
            # 삭제할 때 음료수 이름 입력받고 vending_machine에서 제거, 없으면 없음 출력
            else:
                print(f'{del_input}가 없습니다.')
    # 종료
    elif user_input == '3':
        break
    else:
        print('다시 입력해 주세요.')
