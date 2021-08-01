# 문제: 평균
# 시간: 72ms
import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int,input().split()))
M = max(scores)
print(sum(scores)*100/(M*N))