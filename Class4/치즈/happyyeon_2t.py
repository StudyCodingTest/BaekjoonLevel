import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int,input().split())))

print(cheese)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(cheese,n,m,i,j):
    for i in range(4):
        x = i+dx[i]
        y = j+dy[i]

        if 0<=x<n and 0<=y<m and not visited[x][y]:
            if cheese[x][y] != 0:
                cheese[x][y] += 1
            else:
                visited[x][y] = 1
                dfs(cheese,n,m,x,y)

# 치즈 전체가 0 확인
def check(cheese,n,m):
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                return False
    
    return True
def remove(cheese,n,m):
    for i in range(n):
            for j in range(m):
                # cheese가 3 이상 --> 녹을 예정임
                if cheese[i][j] >=3:
                    cheese[i][j] = 0
                # cheese가 1 혹은 2이다. --> 안 녹음
                elif 1<=cheese[i][j]<3:
                    cheese[i][j] = 1
    return cheese

time = 0
while True:
    if check(cheese,n,m):
        print(time)
        break
    
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    dfs(cheese,n,m,0,0)

    cheese = remove(cheese,n,m)
    # 1초 경과
    time += 1



