import sys
from collections import deque

#BFS 쓸거다
#입력 받아서 그림처럼 그래프화 함
#1을 처음 발견하면 count += 1 하고 BFS해서 0으로 만들어버림. 그러면 visited도 사용 안해도됨  

T = int(sys.stdin.readline())

def bfs(graph, y, x):
    queue = deque()
    queue.append([y, x])
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    #상 하 좌 우 검색
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if N > new_y >= 0 and M > new_x >= 0 and graph[new_y][new_x] == 1:
                graph[new_y][new_x] = 0
                queue.append([new_y, new_x])
                
                
        

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    count = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                bfs(graph, y, x)
                count += 1
    print(count)
                
    
    
