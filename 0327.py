# 리스트
season = ['봄', '여름', '가을', '겨울']

# 리스트 출력
print(season)

# 리스트 인덱싱
print('season[0]', season[0])
print('season[1]', season[1])

# 문자열을 리스트로 변환
text = 'hello'
# 문자열을 리스트로 변환
letters = list(text)

print('letters', letters)

# 리스트 조작
shop = ['반팔', '청바지', '이어폰',
        ['무선 키보드', '유선 키보드', '기계식 키보드']]
# 슬라이싱
print(shop[0:])
# ['반팔', '청바지', '이어폰',
#  ['무선 키보드', '유선 키보드', '기계식 키보드']]
print(shop[:-2])
# ['반팔', '청바지', '이어폰',
#  ['무선 키보드', '유선 키보드', '기계식 키보드']]

# 리스트 수정
shop[0] = '긴팔'
print(shop)

# 리스트 삭제
del shop[0]
print(shop)
# ['청바지', '이어폰', ['무선 키보드', '유선 키보드', '기계식 키보드']]

# 리스트 슬라이싱 삭제
del shop[0:2]
# [['무선 키보드', '유선 키보드', '기계식 키보드']]
print(shop)

# 리스트 더하기
num1 = [1, 2, 3]
num2 = [4, 5, 6]

num1 = num1 + num2
# 리스트 곱하기
print(num1 * 2)  # [1, 2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6]

# 리스트 정렬
num1 = [5, 2, 7, 3]
print('num1', num1)

# 오름차순 정렬
num_asc = sorted(num1)
print('num_asc', num_asc)

# 내림차순 정렬
num_desc = sorted(num1, reverse=True)
print('num_desc', num_desc)

# 리스트 뒤집기
num1.reverse()
print('num1', num1)

# 리스트 조작
num1.append(7)
print('num1', num1)
# 마지막 요소 삭제
num1.pop()
print('num1', num1)
# 인덱스 2 요소 삭제
num1.pop(2)
print('num1', num1)
# 요소 4 삭제
# num1.remove(4)
# print('num1', num1)
# 인덱스 2에 'a' 추가
num1.insert(2, 'a')
print('num1', num1)
# 리스트 초기화
num1.clear()
print('num1', num1)
# 요소 3의 개수
print(num1.count(3))

# 문자열 리스트 조작
text = 'hello, world hello, world ahello, world hello, world'
# 문자열을 리스트로 변환
list1 = list(text)
# 문자열 'a'의 인덱스
print(list1.index('a'))
# 문자열 리스트 뒤집기
list1.reverse()
print('list1', list1)
# 문자열 리스트 정렬
list1_asc = sorted(list1)
# print('list1_asc', list1_asc)

# 리스트 조작
num1 = [1, 2, 3, 4, 5, 6, 1, 1, 1]
print('num1', num1)
# 요소 7 추가
num1.append(7)
print('num1', num1)
# 마지막 요소 삭제
num1.pop()
print('num1', num1)
# 인덱스 2 요소 삭제
num1.pop(2)
print('num1', num1)
# 요소 4 삭제
num1.remove(4)
print('num1', num1)
# 인덱스 2에 'a' 추가
num1.insert(2, 'a')
print('num1', num1)
# 리스트 초기화
num1.clear()
print('num1', num1)
# 요소 3의 개수
print(num1.count(3))

# 실습
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# 1
print(rainbow[2])
# 2.
# 함수
rainbow_asc = sorted(rainbow)
print('rainbow_asc :', rainbow_asc)
# 매서드
rainbow.sort()
print('rainbow :', rainbow)

# 3.
rainbow.insert(7, 'aaa')
print('rainbow :', rainbow)
rainbow.append('bbb')
print('rainbow :', rainbow)

del rainbow[2:6]
print('rainbow :', rainbow)


print()
print()
print()
print()
print()
print()
