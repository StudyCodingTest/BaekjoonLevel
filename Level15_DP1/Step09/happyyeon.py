# 쉬운 계단 수
# 

# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [[0]*10 for _ in range(n+1)]

# # dp[i][j] => N=i이고 맨 앞의 숫자가 j일때 정답 개수
# for i in range(1,n+1) : # N 값
#     for j in range(1,10) : # 맨 앞 숫자
#         # Base Case(N=1)
#         if i == 1 :
#             dp[i][j] = 1
#         # (N=2)
#         # 맨 앞 숫자 = 1~8
#         elif i == 2 and 1<=j<=8 :
#             dp[i][j] = 2
#         # 맨 앞 숫자 = 9
#         elif i == 2 and j == 9 :
#             dp[i][j] = 1
#         # General Case
#         else :
#             if 1<=j<=8 :
#                 dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
#             if j == 9 :
#                 dp[i][9] = dp[i-1][8]
# print(sum(dp[n]) % 1000000000)
N = int(input()) 
dp = [[0]*10 for _ in range(N+1)] 
for i in range(1, 10):
     dp[1][i] = 1 
MOD = 1000000000 
for i in range(2, N+1): 
    for j in range(10): 
        if j == 0: dp[i][j] = dp[i-1][1] 
        elif j == 9: dp[i][j] = dp[i-1][8] 
        else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % MOD)

