# Count linked factor

import sys
from collections import deque

input = sys.stdin.readline

# BFS
def bfs():
    global count
    while queue:
        now = queue.popleft()
        visited[now] = True

        for i in range(len(graph[now])):
            if not visited[graph[now][i]] and not graph[now][i] in queue:
                queue.append(graph[now][i])
    count += 1
    
# Input and varialbes setting
n,m = map(int,input().split())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
visited[0] = True
queue = deque()
count = 0

# Link graph
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

while False in visited:
    queue.append(visited.index(False))
    bfs()

print(count)