# 문제: 숫자의 개수
# 시간: 72ms
import sys
input = sys.stdin.readline

number = 1
for i in range(3):
    number *= int(input())

for num in range(10):
    print(str(number).count(str(num)))