import sys
input = sys.stdin.readline

def solve(n, arr):
    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = arr[0][0]
    dp[1][1] = arr[1][0]

    score = max(arr[0][0], arr[1][0])
    for j in range(2, n + 1):
        dp[0][j] = max(dp[1][j - 1], dp[0][j - 2], dp[1][j - 2]) + arr[0][j - 1]
        dp[1][j] = max(dp[0][j - 1], dp[1][j - 2], dp[0][j - 2]) + arr[1][j - 1]
        score = max(dp[0][j], dp[1][j], score)
    return score

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    print(solve(n, arr))