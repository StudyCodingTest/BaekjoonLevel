# N과 M (1)
# 184ms
from itertools import permutations as P

N, M = map(int, input().split())
for p in P(range(1,N+1),M): print(*p)