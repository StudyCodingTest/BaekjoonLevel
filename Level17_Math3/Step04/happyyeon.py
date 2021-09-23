# 최소공배수
# 76ms
import sys
input = sys.stdin.readline

# 유클리드 호제법 최대공약수
def gcd(a,b) :
    r = a%b
    if r==0 :
        return b
    else : # a와 b의 최대공약수 = b와 r의 최대공약수
        return gcd(b,r)

for _ in range(int(input())) :
    b,a = map(int,input().split())
    print(int(a*b/gcd(a,b))) # a와 b의 최소공배수
