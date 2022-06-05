import sys
from math import gcd
input = sys.stdin.readline

# 최소공배수
def lcm(x,y):
    return x*y // gcd(x,y)

for _ in range(int(input())): # Test case
    m,n,x,y = map(int,input().split()) # M,N,X,Y 입력
    last_num = lcm(m,n)
    
    temp_y = x
    year = x

    while temp_y%n != y%n:
        temp_y = (temp_y+m)%n
        year += m

        if year > last_num:
            break
            
    if year > last_num:
        print(-1)
    else:
        print(year)
    

