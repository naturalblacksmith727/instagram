# 알고리즘 문제 풀이에 자주 쓰이는 파이썬 문법

''' 리스트 컴프리헨션 '''
from functools import reduce
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건문 추가
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 중첩 반복문
coordinates = [(x, y) for x in range(3) for y in range(2)]
print(coordinates)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# if-else 사용
result = ["짝수" if x % 2 == 0 else "홀수" for x in range(5)]
print(result)  # ['짝수', '홀수', '짝수', '홀수', '짝수']

''' 딕셔너리 컴프리헨션 '''
# 기본 형태
squares = {x: x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(squares)

# 조건문 추가
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# 중첩 반복문
coordinates = {(x, y): x + y for x in range(3) for y in range(2)}
# {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2, (2, 0): 2, (2, 1): 3}
print(coordinates)

# if-else 사용
result = {x: "짝수" if x % 2 == 0 else "홀수" for x in range(5)}
print(result)  # {0: '짝수', 1: '홀수', 2: '짝수', 3: '홀수', 4: '짝수'}

'''집합 컴프리헨션'''
# 기본 형태
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 중복 제거
unique_squares = {x**2 for x in range(10) if x % 2 == 0}
print(unique_squares)  # {0, 16, 36, 64}

''' 유용한 파이썬 문법 '''
# 1. enumerate()
# 인덱스와 함께 반복문을 사용할 때 유용
# 인덱스와 값을 동시에 순회할 수 있게 해주는 함수입니다.
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# 0 apple
# 1 banana
# 2 cherry

# 2. zip()
# 두 개 이상의 시퀀스를 병렬로 순회할 때 유용
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
jobs = ['개발자', '디자이너', '마케터']

# zip 사용
for name, age, job in zip(names, ages, jobs):
    print(f"{name}은(는) {age}세이고, {job}입니다.")

# 리스트로 변환
pairs = list(zip(names, ages))
print(pairs)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# 다른 길이의 이터러블
short = [1, 2]
long = [10, 20, 30, 40]
print(list(zip(short, long)))  # [(1, 10), (2, 20)] - 짧은 쪽 기준

# * 연산자로 unzip
pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
unzipped_names, unzipped_ages = zip(*pairs)
print(unzipped_names)  # ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)   # (25, 30, 35)

# 3. sorted()
# 정렬된 새로운 리스트를 반환
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3]

# 내림차순 정렬
reverse_sorted_numbers = sorted(numbers, reverse=True)
print(reverse_sorted_numbers)  # [3, 2, 1]

# 문자열 정렬
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words)
print(sorted_words)  # ['apple', 'banana', 'cherry']

# 4. map()
# 리스트의 각 요소에 함수를 적용하고 결과를 새로운 리스트로 반환
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


# 5. filter()
# 조건에 맞는 요소만 걸러내고 새로운 리스트로 반환
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]


# 6. reduce()
# 초기값과 이터러블의 각 요소에 함수를 적용하여 하나의 결과로 줄이는 함수
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120


# 7. all()
# 모든 요소가 조건을 만족하는지 확인
numbers = [1, 2, 3, 4, 5]
all_even = all(x % 2 == 0 for x in numbers)
print(all_even)  # False


# 8. any()
# 하나 이상의 요소가 조건을 만족하는지 확인
numbers = [1, 2, 3, 4, 5]
any_even = any(x % 2 == 0 for x in numbers)
print(any_even)  # True


# 9. sum()
# 이터러블의 모든 요소를 더하여 합계를 반환
