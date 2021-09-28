# 이항 계수 1
# 76ms
from math import factorial as fact
N, K = map(int, input().split())
print(fact(N)//(fact(N-K)*fact(K)))