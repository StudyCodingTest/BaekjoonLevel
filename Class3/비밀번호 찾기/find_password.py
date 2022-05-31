# Dictionary를 이용한 접근
import sys
sys.stdin = open('input', 'r')

n, m = map(int, input().split())
memo = {}

for _ in range(n):
    site, password = map(str, input().split())
    memo[site] = password

for _ in range(m):
    print(memo[input()])
