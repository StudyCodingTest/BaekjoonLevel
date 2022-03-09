N, M = map(int, input().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# bfs
from collections import deque
visited = [False for _ in range(N+1)]
ans = 0
for node in range(1,N+1):
    if visited[node]:
        continue
    ans += 1
    q = deque([node])
    visited[node] = True
    while q:
        cur_node = q.popleft()
        for adj_node in graph[cur_node]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True
print(ans)

