import sys
from collections import deque
input = sys.stdin.readline

# Connect graph
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
# Setting variables
dx = [0,0,1,-1]
dy = [1,-1,0,0]
count = 0 # shark_move = shark_time
eating = 0 # shark eating sum
x,y,shark_size = 0,0,2

# Find shark_position
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j
# BFS
def bfs(x,y,shark_size):
    visited = [[0]*n for _ in range(n)]
    distance = [[0]*n for _ in range(n)]
    queue =deque()
    queue.append((x,y))
    visited[x][y] = True
    temp = [] # for checking [Left & Upper priority] condition
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                if graph[nx][ny] <= shark_size: # First check can visit
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[cur_x][cur_y] + 1
                
                    if shark_size>graph[nx][ny] and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
        # Priority 1. minimum distance
        # Priority 2. minimum x_position
        # Priority 3. minimum y_position
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))


while True:
    shark_info = bfs(x,y,shark_size)
    # When help mother shark
    if len(shark_info) == 0:
        break
    # Appropriate information , this is satisfied problem condition
    nx,ny,distance = shark_info.pop()
    count += distance
    # Initialize shark_position & fish dead zone
    graph[x][y],graph[nx][ny] = 0,0

    # Now shark_position --> fish dead zone
    x,y = nx,ny
    eating += 1
    if shark_size == eating:
        shark_size += 1
        eating = 0 

print(count)