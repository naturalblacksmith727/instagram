def solution(a, b, c, d):
    answer = 0

    num_list = [a, b, c, d]
    count_list = [num_list.count(x) for x in num_list]

    # 네 주사위 모두 같은 수
    if max(count_list) == 4:
        answer = a * 1111
    elif max(count_list) == 3:
        p = num_list[count_list.index(3)]
        q = num_list[count_list.index(1)]
        answer = (10 * p + q) ** 2
    elif min(count_list) == 2:
        p = max(num_list)
        q = min(num_list)
        answer = (p + q) * abs(p-q)
    elif max(count_list) == 2:
        first_index = count_list.index(1)
        sec_index = count_list.index(1, first_index + 1)
        q = num_list[first_index]
        r = num_list[sec_index]
        answer = q * r
    else:
        answer = min(num_list)
    return answer


solution(2, 2, 2, 2)
solution(4, 1, 4, 4)
solution(6, 3, 3, 6)
solution(2, 5, 2, 6)
solution(6, 4, 2, 5)
