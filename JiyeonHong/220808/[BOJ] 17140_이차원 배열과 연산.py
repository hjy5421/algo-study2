from collections import defaultdict

def solution(r, c, k):
    time = 0
    if r - 1 < len(A) and c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        return time

    while time <= 100:
        countR, countC = len(A), len(A[0])
        if countR >= countC:
            calculate_R()
        else:
            calculate_C()
        time += 1
        #초기 배열보다 r,c가 클 수도 있어서 범위 체크 필요
        if r-1<len(A) and c-1<len(A[0]) and A[r-1][c-1] ==k:
            break

    if time>100:
        time=-1
    return time


def calculate_R():
    sort_A = []
    maxlen = 0
    global A
    for i in range(len(A)):
        arr = sorting(i, True)
        maxlen = max(maxlen, len(arr))
        sort_A.append(arr)

    for i in range(len(sort_A)):
        if len(sort_A[i]) == maxlen:
            continue
        tmp_zero = [0 for _ in range(maxlen - len(sort_A[i]))]
        sort_A[i].extend(tmp_zero)
    A = [items[:] for items in sort_A]


def calculate_C():
    sort_A = []
    maxlen = 0
    global A
    for i in range(len(A[0])):
        arr = sorting(i, False)
        maxlen = max(maxlen, len(arr))
        sort_A.append(arr)

    for i in range(len(sort_A)):
        if len(sort_A[i]) == maxlen:
            continue
        tmp_zero = [0 for _ in range(maxlen - len(sort_A[i]))]
        sort_A[i].extend(tmp_zero)

    A = [[0 for _ in range(len(sort_A))] for _ in range(len(sort_A[0]))]
    for i in range(len(sort_A)):
        for j in range(len(sort_A[i])):
            A[j][i] = sort_A[i][j]


def sorting(idx, isRow):
    arr = []
    if isRow:
        arr = A[idx][:]
        arr = copy_list(arr)
    else:
        arr = [A[i][idx] for i in range(len(A))]
        arr = copy_list(arr)

    arr_dict = defaultdict(int)  # 숫자 : 등장횟수
    for num in arr:
        arr_dict[num] += 1

    arr_appearing = []
    for num in arr_dict.keys():
        arr_appearing.append((num, arr_dict[num]))
    # 등장 횟수순, 수 오름차순으로 정렬
    arr_appearing = sorted(arr_appearing, key=lambda x: (x[1], x[0]))

    arr = []
    for num in arr_appearing:
        arr.extend([num[0], num[1]])
    return arr


def copy_list(origin):
    copy = []
    for i in range(len(origin)):
        if i >= 100:
            break
        if origin[i] == 0:
            continue
        copy.append(origin[i])
    return copy[:]


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    global A
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))
    print(solution(r, c, k))
