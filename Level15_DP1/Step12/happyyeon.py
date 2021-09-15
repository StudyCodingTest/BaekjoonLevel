# 가장 긴 바이토닉 부분 수열
# 360ms

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a_reverse = a[::-1] # dp_decrease를 위하여
dp_increase = [1]*n # DP memoization 초기화 , dp_increase[0] = 1
dp_decrease = [1]*n 
dp_sum = [0]*n # dp_increase + dp_decrease
# 가장 긴 증가하는 부분 수열
for i in range(n) :
    for j in range(i) :
        if a[i] > a[j] :
            dp_increase[i] = max(dp_increase[i],dp_increase[j]+1)
# 가장 긴 감소하는 부분 수열 
for i in range(n) :
    for j in range(i) :
        if a_reverse[i] > a_reverse[j] :
            dp_decrease[i] = max(dp_decrease[i],dp_decrease[j]+1)

dp_decrease = dp_decrease[::-1]

# 바이토닉 = 증가 + 감소 - 1
for i in range(n) :
    dp_sum[i] = dp_increase[i] + dp_decrease[i] -1

print(max(dp_sum))
