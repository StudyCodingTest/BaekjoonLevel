# N과 M (3)
# 1776ms
from itertools import product as PI

N, M = map(int, input().split())
for pi in PI(*([range(1,N+1)]*M)): print(*pi)