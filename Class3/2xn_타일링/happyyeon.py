import sys
input = sys.stdin.readline

n = int(input())

# dp[n]: 2xn 사각형을 채우는 경우의 수
# dp[n] = dp[n-1] + dp[n-2]
dp = [0]*1001
dp[1],dp[2] = 1,2

for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)