# 9372. 상근이의 여행
import sys
input = sys.stdin.readline
from collections import deque

for tc in range(int(input())):
    N, M = map(int, input().rstrip().split())
    graph = {i:[] for i in range(1,N+1)}
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(N+1)]
    q = deque([1])
    visited[1] = True
    cnt = 0
    while q:
        cur_node = q.popleft()
        for adj_node in graph[cur_node]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True
                cnt += 1
    print(cnt) # N-1