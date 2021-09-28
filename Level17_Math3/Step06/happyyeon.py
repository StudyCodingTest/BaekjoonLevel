# 링
# 168ms

import sys
from fractions import Fraction
input = sys.stdin.readline

# 기약 분수 -> (분자//gcd) / (분모 // gcd)
def gcd(a, b):
    while(b != 0):
        n = a%b
        a = b
        b = n
    return a

n = int(input())
radiuses = list(map(int,input().split())) #[r0, r1, r2 ,...]

for i in range(1,n) : # 원 r1, 원 r2 ,... 에 대하여
    devider = gcd(radiuses[0],radiuses[i])
    print("{0}/{1}".format(radiuses[0]//devider, radiuses[i]//devider))

