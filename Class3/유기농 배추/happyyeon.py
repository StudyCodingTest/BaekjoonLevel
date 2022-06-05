import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    m,n,k = map(int,input().split())

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def bfs(graph,a,b):
        q = deque([(a,b)])
        graph[a][b] = 0

        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < n and 0<= ny < m and graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
    
    count = 0
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        y,x = map(int,input().split())
        graph[x][y] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                count += 1
    
    print(count)
