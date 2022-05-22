import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
# 초기 조건
m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]

q = deque()
# stack = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
            stack.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(tomato):
    while q:
        i,j = q.popleft()

        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]
        
            if 0<=x<n and 0<=y<m and tomato[x][y] == 0:
                tomato[x][y] = tomato[i][j] + 1
                q.append((x,y))

# def dfs(tomato):
#     while stack:
#         i,j = stack.pop()

#         for k in range(4):
#             x = i+dx[k]
#             y = j+dy[k]

#             if 0<=x<n and 0<=y<m and tomato[x][y] == 0:
#                 tomato[x][y] = tomato[i][j] + 1
#                 stack.append((x,y))

def check_zero(tomato):
    for i in tomato:
        if 0 in i:
            return True
    return False

def check_day(tomato):
    day = -1*INF

    for i in tomato:
        day = max(max(i),day)
    return day


bfs(tomato)


if check_zero(tomato):
    print(-1)
else:
    print(check_day(tomato)-1)
        
