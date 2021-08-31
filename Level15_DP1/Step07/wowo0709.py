# 계단 오르기
# 88ms
n = int(input())
# 계단 점수, 전계단 안 밟은 최대 점수, 전계단 밟은 최대 점수
stairs = [[0,0,0]]+[[int(input()),0,0] for _ in range(n)]
stairs[1][1] = stairs[1][2] = stairs[1][0]
for i in range(2,n+1):
    stairs[i][1] = stairs[i][0] + max(stairs[i-2][1:])
    stairs[i][2] = stairs[i][0] + stairs[i-1][1]
print(max(stairs[-1][1:]))

