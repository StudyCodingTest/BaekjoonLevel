# 나이순 정렬
# 284ms
import sys
input = sys.stdin.readline
members = []
for _ in range(int(input())): 
    age, name = input().split()
    members.append((int(age),name))
members.sort(key=lambda m: m[0])
for member in members: print(*member)