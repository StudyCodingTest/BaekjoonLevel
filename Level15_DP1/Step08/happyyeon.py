# 1로 만들기
# 660ms

import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1) # memoization

# dp(N) = min(dp(N//3)+1, dp(N//2)+1, dp(N-1)+1)
for i in range(2,n+1) :
    # -1 먼저
    dp[i] = dp[i-1] + 1
    # -1을 뺀 케이스와 N//2를 한 케이스와 누가 더 경우의 수가 작을까 ?
    if i%2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    # -1을 뺀 케이스와 N//2와 N//3 중 어느 케이스의 경우의 수가 제일 작을까 ?
    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
    
print(dp[n])
