# 01타일
# 460ms

import sys
input = sys.stdin.readline
n = int(input())

dp = [0]* 1000001 
dp[1] = 1
dp[2] = 2

for num in range(3,n+1) :
    dp[num] = (dp[num-1] + dp[num-2]) % 15746

print(dp[n])


# import sys
# input = sys.stdin.readline
# n = int(input())

# sys.setrecursionlimit(10**6)

# # 팩토리얼 함수
# def get_factorial(num) :  
#     if num == 0 or num == 1 :
#         return 1

#     return num * get_factorial(num-1)
# # 타일 배치 경우의 수 구하는 함수
# def get_num_case(n) :
#     num_zero_zero = 0 # 00의 개수
#     sum_case = 0
#     while num_zero_zero <= (n//2) :
#         # (N-["00의 개수"])! / ("00"의 개수)!("1"의 개수)
#         sum_case += (get_factorial(n-num_zero_zero) / (get_factorial(num_zero_zero)*get_factorial(n - 2*num_zero_zero))) % 15746
#         num_zero_zero += 1
    
#     return sum_case

# print(int(get_num_case(n)))


























# sys.setrecursionlimit(10**6)

# # 팩토리얼 함수
# def get_factorial(num) :  
#     if num == 0 or num == 1 :
#         return 1

#     return num * get_factorial(num-1)
# # 타일 배치 경우의 수 구하는 함수
# def get_num_case(n) :
#     num_zero_zero = 0 # 00의 개수
#     sum_case = 0
#     while num_zero_zero <= (n//2) :
#         # (N-["00의 개수"])! / ("00"의 개수)!("1"의 개수)
#         sum_case += get_factorial(n-num_zero_zero) / (get_factorial(num_zero_zero)*get_factorial(n - 2*num_zero_zero))
#         num_zero_zero += 1
    
#     return sum_case

# print(int(get_num_case(n)%15746))