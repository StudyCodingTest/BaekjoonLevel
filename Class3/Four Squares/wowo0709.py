N = int(input())
dp = [float('inf') for _ in range(N+1)]
dp[0], dp[1] = 0, 1
for i in range(N+1):
    for j in range(1,int(i**(1/2))+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[N])

# 시간 초과
# N = int(input())
# dp = [float('inf') for _ in range(N+1)]
# dp[0], dp[1] = 0, 1
# for i in range(2,N+1):
#     if int(i**(1/2)) == i**(1/2):
#         dp[i] = 1
#         continue
#     for j in range(1,i//2+1):
#         dp[i] = min(dp[i],dp[j]+dp[i-j])
#         if dp[i] == 2: break
# print(dp[N])