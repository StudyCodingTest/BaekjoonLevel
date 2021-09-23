# ATM
# 72ms

import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split())) # p = [3,1,4,3,2]
p.sort() # p = [1,2,3,3,4]

dp = [0]*1001
dp[1] = p[0]

for i in range(2,n+1) : # dp = [p[1], p[2]+dp[1], p[3]+dp[2], p[4]+dp[3], ...] , dp[i] = i번 사람의 총 대기 시간
    dp[i] = p[i-1] + dp[i-1]

print(sum(dp[1:n+1])) # 1+(1+2)+(1+2+3)+(1+2+3+3)+(1+2+3+3+4)