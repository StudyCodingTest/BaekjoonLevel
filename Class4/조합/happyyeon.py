import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 초기 조건
n,m = map(int,input().split())

arr_fact = [1]*101

# n!
for i in range(2,101):
    arr_fact[i] = i*arr_fact[i-1]

answer = arr_fact[n]//(arr_fact[n-m]*arr_fact[m])
print(answer)




