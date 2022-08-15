import heapq
from collections import deque, defaultdict

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * N * 2)


def solution():
    turn = 1
    while True:
        belt.rotate(1)
        robot.rotate(1)
        robot[N-1]=0
        for i in range(N - 2, 0, -1):
            if robot[i]==1 and belt[i + 1] > 0 and robot[i + 1] == 0:
                robot[i] = 0
                robot[i + 1] = 1
                belt[i + 1] -= 1
        robot[N - 1] = 0
        if belt[0] > 0:
            robot[0] = 1
            belt[0] -= 1
        if belt.count(0) >= K:
            break
        turn += 1
    return turn


print(solution())
