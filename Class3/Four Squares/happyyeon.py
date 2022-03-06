# Four Squares
# 144ms
import sys

input = sys.stdin.readline

# Input and variable setting
n = int(input())
dp = [0,1]

for i in range(2,n+1):
    #1. Find minimum --> dp[n-1^2],dp[n-2^2],...,dp[n-square num] 
    min_value = 1e9
    j = 1

    while (j**2)<=i:
        min_value = min(min_value,dp[i-j**2])
        j += 1
    #2. #1 + ADD 1 ==> dp[i]
    dp.append(min_value+1)

print(dp[n])




# error code using greedy approach.. 
# count = 0
# # 223^2 = 49729 --> the nearest number 50000
# #1. Save 1~223 square number
# squares = [0]*224
# for i in range(1,224):
#     squares[i] = i**2

# while n>0:
#     #2. Find "What is max item satisfied [item <= n]?" ex) 27 --> 5^2
#     item = max([i for i in range(224) if squares[i]<=n]) # 5
#     count += 1 # increase counting

#     #3. Again n = [n-item^2]
#     n -= item**2
    
# #4. if [n-item^2] = 0 --> stop!
# print(count)



