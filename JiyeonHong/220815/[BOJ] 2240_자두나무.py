T, W = map(int, input().split())
turns = []
for _ in range(T):
    turns.append(int(input().strip()))
'''
dp[떨어지는 시간][최대 움직일 수 있는 횟수][자두나무 위치]

dp[t][w][1]
자두가 1번 나무에서 떨어지는 경우
- 1번 -> 1번 = dp[t-1][w][1]+1
- 2번 -> 1번 = dp[t-1][w-1][2]+1

dp[t][w][2]
자두가 2번 나무에서 떨어지는 경우
- 2번 -> 2번 = dp[t-1][w][2]+1
- 1번 -> 2번 = dp[t-1][w-1][1]+1

'''


def solution():
    dp = [[[0 for _ in range(3)] for _ in range(W + 1)] for _ in range(T + 1)]

    for i in range(1, T + 1):
        for j in range(0, W + 1):
            if turns[i - 1] == 1:  # 자두가 1번 나무에서 떨어지는 경우
                if j == 0:
                    dp[i][j][1] = dp[i - 1][j][1] + 1
                    continue
                dp[i][j][1] = max(dp[i - 1][j][1] + 1, dp[i - 1][j - 1][2] + 1)
                dp[i][j][2] = max(dp[i - 1][j - 1][1], dp[i - 1][j][2])
            else:  # 자두가 2번 나무에서 떨어지는 경우
                if j == 0:
                    dp[i][j][1] = dp[i - 1][j][1]
                    continue
                dp[i][j][1] = max(dp[i - 1][j - 1][2], dp[i - 1][j][1])
                dp[i][j][2] = max(dp[i - 1][j][2] + 1, dp[i - 1][j - 1][1] + 1)

    answer = 0
    for i in range(W + 1):
        answer = max(answer, dp[T][i][1])
        answer = max(answer, dp[T][i][2])
    return answer


print(solution())
