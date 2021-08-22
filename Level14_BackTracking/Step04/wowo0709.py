# N과 M (4)
# 80ms
from itertools import combinations_with_replacement as H

N, M = map(int, input().split())
for h in H(range(1,N+1),M): print(*h)