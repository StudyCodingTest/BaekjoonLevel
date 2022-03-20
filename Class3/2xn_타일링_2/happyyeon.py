import sys
input = sys.stdin.readline

# 초기값 세팅
n = int(input())
dp = [1]*1001
dp[2] = 3

# dp 배열 생성
# dp[n] = dp[n-1] + 2dp[n-2]
for i in range(3,1001):
    dp[i] = (dp[i-1] + 2*dp[i-2])%10007

print(dp[n])