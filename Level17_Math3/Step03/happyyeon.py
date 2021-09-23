# 최대공약수와 최소공배수
# 72ms

import sys
input = sys.stdin.readline

a,b = map(int,input().split())
devider = min(a,b) # devider : 18->17->16->...->3->2->1
gcd = 1 # 최대공약수 초기화
max_val = max(a,b)
min_val = min(a,b)
lcm = max_val # 최소 공배수 초기화
# 최대공약수
while devider > 1:
    if a%devider==0 and b%devider==0 :
        a = a//devider
        b = b//devider
        gcd = gcd*devider
    else :
        devider -= 1

# 최소공배수
while lcm%min_val !=0 : # devider :  a,b중 작은 수
    lcm += max_val

print(gcd)
print(lcm)
