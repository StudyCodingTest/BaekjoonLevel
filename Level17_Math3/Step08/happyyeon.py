# 이항 계수 2
# 496ms

import sys
input = sys.stdin.readline

dp = [[1] for _ in range(1001)]
dp[1].append(1)
for i in range(2,1001) :
    for j in range(1,1000) :
        if j == i :
            dp[i].append(1)
        if 0 < j < i :
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])

n,k = map(int,input().split())
print(dp[n][k]%10007)