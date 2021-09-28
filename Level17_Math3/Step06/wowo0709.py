# 링
# 84ms
from math import gcd

N = int(input())
rs = list(map(int, input().split()))

for i in range(1,len(rs)):
    _gcd = gcd(rs[0],rs[i])
    print(str(rs[0]//_gcd)+'/'+str(rs[i]//_gcd))