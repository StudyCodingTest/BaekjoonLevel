# 쉬운 계단 수
# 68ms
import sys
input = sys.stdin.readline

n = int(input())
# dp[숫자길이][맨앞숫자] = 경우의 수 
dp = [[0]*10 for _ in range(n+1)] 
# 숫자길이 = 1 , 경우의 수 = 1
for i in range(1, 10):
     dp[1][i] = 1  
for i in range(2, n+1): 
    for j in range(10):
        # 맨앞 숫자가 0 or 9 
        if j == 9: 
            dp[i][j] = dp[i-1][8] 
        elif j == 0: 
            dp[i][j] = dp[i-1][1] 
        # 맨앞 숫자가 1~8
        else: 
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[n]) % 1000000000)

