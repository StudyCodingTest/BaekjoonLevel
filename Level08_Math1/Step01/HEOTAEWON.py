#문제: 손익분기점, 시간: 72ms
import sys


static, flexible, price = map(int, sys.stdin.readline().split())
print(static, flexible, price)

total_price = static
count = price - flexible
if flexible >= price:
    print(-1)
else:
    print(total_price//count + 1)
