import sys
from collections import deque
input = sys.stdin.readline

# 초기 조건
node,edge,start = map(int,input().split())
graph = [[] for _ in range(node+1)]
for _ in range(edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(node+1):
    graph[i].sort()
visited = [0]*(node+1)

def get_next_node(visited,cur_node):
    for i in graph[cur_node]:
        if visited[i] == 0:
            return i
    return False

# DFS
def dfs(start):
    print(start,end=" ")
    visited[start] = 1

    for next_node in graph[start]:
        if visited[next_node] == 0:
            dfs(next_node)

# BFS
def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        cur_node = q.popleft()
        print(cur_node, end=" ")

        for next_node in graph[cur_node]:
            if visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = 1

dfs(start)
print()
visited=[0]*(node+1)
bfs(start)
     
