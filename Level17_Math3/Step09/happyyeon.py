# 다리 놓기
# 84ms

from math import comb
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n,m = map(int,input().split())
    print(comb(m,n))