# 검문
# 72ms
N = int(input())
nums = [int(input()) for _ in range(N)]

from math import gcd
_gcd = gcd(abs(nums[0] - nums[-1]))
for i in range(1,len(nums)):
    _gcd = gcd(_gcd,abs(nums[i]-nums[i-1]))
    
ans = set([_gcd])
for n in range(2,int(_gcd**(1/2))+1):
    if _gcd % n == 0:
        ans.add(n)
        ans.add(_gcd//n)

print(*sorted(list(ans)))