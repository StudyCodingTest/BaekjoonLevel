dp = [0 for _ in range(11)]
dp[1], dp[2], dp[3] = 1, 2, 4 # 1 # 1+1, 2 # 1+1+1, 1+2, 2+1, 3
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for _ in range(int(input())):
    print(dp[int(input())])