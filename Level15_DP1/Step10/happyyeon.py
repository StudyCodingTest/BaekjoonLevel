# 포도주 시식
# 80ms
# https://www.acmicpc.net/board/view/60664 , 도움 받은 설명
import sys
input = sys.stdin.readline

n = int(input())
alcohols = [0]*10001 # 포도주들
sums_alcohols = [0]*10001 # 포도주의 누적 총량
for i in range(n) :
    alcohols[i] = int(input())

# Base Case
sums_alcohols[0] = alcohols[0]
sums_alcohols[1] = alcohols[0]+alcohols[1]
sums_alcohols[2] = max(alcohols[2]+alcohols[0],alcohols[2]+alcohols[1], sums_alcohols[1]) #(포도주 마셨을때와 마시지 않았을 때로 나눔)
# General Case
for i in range(3,n) :
    sums_alcohols[i] = max((sums_alcohols[i-2] + alcohols[i]), (sums_alcohols[i-3]+alcohols[i-1]+alcohols[i]), sums_alcohols[i-1])

print(sums_alcohols[n-1])