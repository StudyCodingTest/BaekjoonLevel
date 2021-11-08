# matrix multiplication
# 

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a= []
for _ in range(n):
    a.append(list(map(int,input().split())))

m,k = map(int,input().split())
b= []
for _ in range(m):
    b.append(list(map(int,input().split())))

# matrix c: NxK matrix
c = [[0]*k for _ in range(n)]

# matrix multiplication
for i in range(n):
    for j in range(k):
        for x in range(m):
            c[i][j] += a[i][x] * b[x][j]

for i in range(n):
    print(*c[i])


