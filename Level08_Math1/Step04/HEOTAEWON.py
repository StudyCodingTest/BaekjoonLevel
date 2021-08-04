#문제: 달팽이는 올라가고 싶다, 시간: 84ms
import sys


a, b, v = map(int, sys.stdin.readline().split())
days = 0
v -= b
climb = a-b

days = v/climb
if days%1 == 0:
    print(int(days))
else:
    print(int(days)+1)
if v < climb:
    days += 1

#if v%climb == 0:
 #   days -= 1
#else:
 #   days += 1

#print(days)



