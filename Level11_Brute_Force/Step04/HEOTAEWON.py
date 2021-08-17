#문제: 체스판 다시 칠하기
#번호: 1018
#시간:


import sys


n, m = map(int, sys.stdin.readline().split())
ches = []
for _ in range(n):
    ches.append(list(map(str, sys.stdin.readline().split())))
print(ches)

