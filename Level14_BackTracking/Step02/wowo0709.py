# N과 M (2)
# 72ms
from itertools import combinations as C

N, M = map(int, input().split())
for c in C(range(1,N+1),M): print(*c)