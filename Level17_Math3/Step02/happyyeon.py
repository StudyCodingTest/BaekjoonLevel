# 약수
# 72ms

# ex) 50 -> 1,2,5,10,25,50
import sys
input = sys.stdin.readline

num = int(input())
divisors = list(map(int,input().split())) # [5,2,25,10]
divisors.sort() # [2,5,10,25]

print(divisors[0]*divisors[-1])