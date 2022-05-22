import sys

n, m = map(int, sys.stdin.readline().split())

dp = [[0]*101 for _ in range(101)]

for i in range(n):
    for j in range(i+1):
        if i == j:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = i + 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][m-1])