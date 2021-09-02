# 계단 오르기
# 68ms

import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]*300 # 계단들
sums_stair = [0]*300 # 해당 계단의 경로 누적합
for i in range(n) :
    stairs[i] = int(input())

# Base Case
sums_stair[0] = stairs[0]
sums_stair[1] = stairs[0]+stairs[1]
sums_stair[2] = stairs[2] + max(stairs[0],stairs[1])
# General Case
for i in range(3,n) :
    sums_stair[i] = max((sums_stair[i-2] + stairs[i]), (sums_stair[i-3]+stairs[i-1]+stairs[i]))

print(sums_stair[n-1])