# 이항 계수 1
# 80ms

from math import comb
import sys
input = sys.stdin.readline
n,k = map(int,input().split())

print(comb(n,k))

