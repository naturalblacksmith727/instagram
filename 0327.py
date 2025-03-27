"""
리스트
    1. 리스트 생성
    2. 리스트 인덱싱
    3. 문자열을 리스트로 변환
    4. 리스트 조작
    5. 리스트 슬라이싱
    6. 리스트 수정
    7. 리스트 삭제
"""


# 1. 리스트 생성
season = ['봄', '여름', '가을', '겨울']

# 리스트 출력
print(season)

# 2. 리스트 인덱싱
print('season[0]', season[0])
print('season[1]', season[1])

# 3. 문자열을 리스트로 변환
text = 'hello'
# 문자열을 리스트로 변환
letters = list(text)

print('letters', letters)

# 4. 리스트 조작
shop = ['반팔', '청바지', '이어폰',
        ['무선 키보드', '유선 키보드', '기계식 키보드']]
# 5. 리스트 슬라이싱
print(shop[0:])
# ['반팔', '청바지', '이어폰',
#  ['무선 키보드', '유선 키보드', '기계식 키보드']]
print(shop[:-2])
# ['반팔', '청바지', '이어폰',
#  ['무선 키보드', '유선 키보드', '기계식 키보드']]

# 6. 리스트 수정
shop[0] = '긴팔'
print(shop)

# 7. 리스트 삭제
del shop[0]
print(shop)
# ['청바지', '이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# 8. 리스트 슬라이싱 삭제
del shop[0:2]
# [['무선 키보드', '유선 키보드', '기계식 키보드']]
print(shop)

# 9. 리스트 더하기
num1 = [1, 2, 3]
num2 = [4, 5, 6]

num1 = num1 + num2
# 10. 리스트 곱하기
print(num1 * 2)  # [1, 2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6]

# 11. 리스트 정렬
num1 = [5, 2, 7, 3]
print('num1', num1)

# 12. 오름차순 정렬
num_asc = sorted(num1)
print('num_asc', num_asc)

# 13. 내림차순 정렬
num_desc = sorted(num1, reverse=True)
print('num_desc', num_desc)

# 14. 리스트 뒤집기
num1.reverse()
print('num1', num1)

# 15. 리스트 조작
num1.append(7)
print('num1', num1)
# 16. 마지막 요소 삭제
num1.pop()
print('num1', num1)
# 17. 인덱스 2 요소 삭제
num1.pop(2)
print('num1', num1)
# 18. 요소 4 삭제
"""
remove() 메서드는 첫 번째 일치하는 요소를 삭제
remove() 메서드는 요소가 없으면 오류 발생
"""
# num1.remove(4)
# print('num1', num1)
# 19. 인덱스 2에 'a' 추가
num1.insert(2, 'a')
print('num1', num1)
# 20. 리스트 초기화
num1.clear()
print('num1', num1)
# 21. 요소 3의 개수
print(num1.count(3))

# 22. 문자열 리스트 조작
text = 'hello, world hello, world ahello, world hello, world'
# 23. 문자열을 리스트로 변환
list1 = list(text)
# 24. 문자열 'a'의 인덱스
print(list1.index('a'))
# 25. 문자열 리스트 뒤집기
list1.reverse()
print('list1', list1)
# 26. 문자열 리스트 정렬
list1_asc = sorted(list1)
# print('list1_asc', list1_asc)

# 27. 리스트 조작
num1 = [1, 2, 3, 4, 5, 6, 1, 1, 1]
print('num1', num1)
# 28. 요소 7 추가
num1.append(7)
print('num1', num1)
# 29. 마지막 요소 삭제
num1.pop()
print('num1', num1)
# 30. 인덱스 2 요소 삭제
num1.pop(2)
print('num1', num1)
# 31. 요소 4 삭제
num1.remove(4)
print('num1', num1)
# 32. 인덱스 2에 'a' 추가
num1.insert(2, 'a')
print('num1', num1)
# 33. 리스트 초기화
num1.clear()
print('num1', num1)
# 34. 요소 3의 개수
print(num1.count(3))

# 실습
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# 1.실습
print(rainbow[2])
# 2.실습
# 함수
rainbow_asc = sorted(rainbow)
print('rainbow_asc :', rainbow_asc)
# 매서드
rainbow.sort()
print('rainbow :', rainbow)

# 3.실습
rainbow.insert(7, 'aaa')
print('rainbow :', rainbow)
rainbow.append('bbb')
print('rainbow :', rainbow)

del rainbow[2:6]
print('rainbow :', rainbow)

"""
이차원 리스트
    1. 행렬
    2. 행렬 인덱싱
    3. 행렬 수정
    4. 행 추가
    5. 요소 수정
    6. 행 삭제
"""

# 1. 행렬
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. 행렬 인덱싱
value = matrix[1][2]
print('matrix[1][2]', value)

# 3. 행렬 수정
matrix[1] = matrix[1] + [100]
print(matrix)

# 4. 행 추가
matrix = matrix + [[10, 11, 12]]
print('행 추가', matrix)

# 5. 요소 수정
matrix[0][0] = 11
matrix[1][1] = 22
matrix[2][2] = 33
print('요소 수정 : ', matrix)

# 6. 행 삭제
del matrix[1]
print('del matrix[1] :', matrix)

# 7. 요소 삭제
del matrix[1][1]
print('del matrix[1][1] :', matrix)

# 8. 행의 개수
rows = len(matrix)
print('행의 개수:', rows)
# 9. 열의 개수
cols = len(matrix[0])
print('열의 개수:', rows)

# 10. 행을 추가
matrix.append([11, 22, 33])
print('행 추가 : ', matrix)
# 11. 요소 추가
matrix[1].append(22)
print('요소 추가 : ', matrix)
# 12. 행 추가
matrix.insert(2, [11, 11, 11])
print('행 추가 : ', matrix)
# 13. 요소 추가
matrix[1].insert(2, 11111)
print('요소 추가 : ', matrix)
# 14. 요소 확장
matrix[0].extend([55, 66])
print('요소 확장 : ', matrix)

"""
        튜플
    1. 튜플 생성
    2. 튜플 인덱싱
    3. 튜플 수정
    4. 튜플 추가
    5. 튜플 삭제
    6. 튜플 조작
"""
# 튜플 생성
t1 = (1, 2, 3, 4, 5)
print('t1 :', t1)
# 튜플 생성
t2 = tuple((1, 2, 3, 4, 5))
print('t2 :', t2)

# 튜플 생성
t3 = 1, 2, 3, 4, 5
print('t3 :', t3)

# 튜플 생성
t4 = 1,
print('t4 :', t4)

# 튜플 생성
t5 = (1)
print('t5 :', t5)

# 튜플 생성
t6 = (1,)
print('t6 :', t6)

# 튜플 인덱싱
print('t1[0]', t1[0])
print('t1[1]', t1[1])

# 튜플 수정
t1 = t1 + (6, 7, 8)
print('t1 :', t1)

# 튜플 삭제
# del t1
# print('t1 :', t1)

# 튜플 조작
t1 = t1 + (6, 7, 8)
print('t1 :', t1)

# 튜플 조작
t1 = t1 * 2
print('t1 :', t1)

"""
셋 (set)
    1. 셋 생성
    2. 셋 요소 추가
    3. 셋 요소 삭제
    4. 셋 요소 조회
    5. 셋 요소 수정
    6. 셋 요소 제거
"""
# 셋 (set)
# 1. 셋 생성
s1 = {1, 2, 3, 4, 4, 2}
print('s1 :', s1)
# 2. 셋 생성
s2 = set((1, 2, 3, 3, 3, 3, 6, 6, 6, 7, 7, 7))
print('s2:', s2)
# 3. 셋 생성
s3 = set([11, 2, 4, 7])
print('s3:', s3)
# 4. 요소 추가
s1.add(5)
print('s1 :', s1)
# 5. 요소 추가
s1.update([2, 2, 3, 3, 5, 5, 6, 6])
print('s1 :', s1)

""" 
        remove() 메서드는 셋에 요소가 없으면 오류 발생
        discard() 메서드는 셋에 요소가 없으면 무시
"""
# 6. 요소 삭제
s1.remove(3)
print('s1 :', s1)
# 7. 요소 삭제
s1.discard(7)
print('s1 :', s1)
# 8. 셋 초기화
s1.clear()
print('s1 :', s1)
print('s2 :', s2)

# 9. 합집합
s7 = s1 | s2
print('s7 :', s7)
# 10. 합집합
s7 = s1.union(s2)
print('s7 :', s7)

# 11. 합집합
s10 = s1 | s2 | s3
print('s10:', s10)
# 12. 합집합
s10 = s1.union(s2).union(s3)
print('s10:', s10)

# 13. 교집합
s4 = s1 & s2
print('s4 :', s4)
# 14. 교집합
s4 = s1.intersection(s2)
print('s4 :', s4)

# 15. 차집합
s5 = s1 - s2
print('s5:', s5)
# 16. 차집합
s5 = s1.difference(s2)
print('s5:', s5)

# 17. 차집합
s6 = s2 - s1
print('s6:', s6)
# 18. 차집합
s6 = s2.difference(s1)
print('s6:', s6)

# 19. 교집합
print(s1 & s3 - s2)

"""
딕셔너리
    1. 빈 딕셔너리
    2. 빈 딕셔너리
    3. 딕셔너리 생성
    4. 요소 접근
    5. 요소 수정
    6. 요소 삭제
"""
# 1. 빈 딕셔너리
dict1 = {}
print('dict1 :', dict1)
# 2. 빈 딕셔너리
dict2 = dict()
print('dict2:', dict2)

# 3. 딕셔너리 생성
dict1 = {
    'name': '홍길동',
    'age': 30,
    'city': ["서울", "은평구"]
}
print('dict1 :', dict1)
# 4. 딕셔너리 생성
dict2 = dict(name='홍길동', age=30, city='서울')
print('dict2:', dict2)

# 5. 요소 접근
print('dict1[name] :', dict1['name'])
print('dict1[city] :', dict1['city'][1])
print('dict1[age] :', dict1['age'])

# 6. 수정
dict1["age"] = 31
print('dict1[age] :', dict1['age'])
print('dict1 :', dict1)

# 7. 추가
dict1["생년월일"] = 20000101
print('dict1[생년월일] :', dict1['생년월일'])
# 8. 추가
dict1["hobby"] = ["캠핑", '등산', '런닝']
print('dict1 :', dict1)

# 9. 삭제
del dict1['hobby']
print('dict1 :', dict1)

# 10. 딕셔너리 키 조회
fruits = {'apple': '사과', 'banana': '바나나', }
print('fruits :', fruits)
print("fruits.get('apple') :", fruits.get('apple'))
print("fruits.get('peach') :", fruits.get('peach'))
"""
get() 메서드는 키가 없으면 None을 반환
get() 메서드는 키가 있으면 키에 해당하는 값을 반환
"""
# 11. 딕셔너리 요소 추가
print("fruits.get('peach','복숭아') :", fruits.get('peach', '복숭아'))

# 12. 딕셔너리 요소 추가
fruits.update({'apple': '사과', 'grapes': '포도', 'melon': '멜론'})
print('fruits :', fruits)

# 13. 딕셔너리 키 조회
print(fruits.keys())
# 14. 딕셔너리 값 조회
print(fruits.values())
# 15. 딕셔너리 키와 값 조회
print(fruits.items())

# 16. 딕셔너리 초기화
fruits.clear()
print('fruits :', fruits)

student_dict = {"Alice": 85, "Bob": 90, "charlie": 95}

student_dict.update({"David": 80})
print(student_dict)

student_dict.update({"Alice": 88})
print(student_dict)

del student_dict["Bob"]
print(student_dict)

print()
print()
print()
print()
print()
print()
