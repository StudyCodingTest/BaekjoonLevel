# 가장 긴 증가하는 부분 수열
# 204ms

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp = [1]*n # DP memoization 초기화 , dp[0] = 1

# 발견한 점화식
for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

