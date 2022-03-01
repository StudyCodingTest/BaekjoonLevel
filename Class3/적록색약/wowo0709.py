from collections import deque
didj = [(-1,0), (1,0), (0,-1), (0,1)]
def bfs(cur, state):
    if visited[state][cur[0]][cur[1]]:
        return 0
    q = deque([])
    q.append(cur)
    visited[state][cur[0]][cur[1]] = True
    c = MAP[cur[0]][cur[1]]
    if state == 'RG/B' and c in 'RG': c = 'RG'
    while q:
        cur = q.popleft()
        for di, dj in didj:
            new_i, new_j = cur[0]+di, cur[1]+dj
            if 0<=new_i<N and 0<=new_j<N and MAP[new_i][new_j] in c and not visited[state][new_i][new_j]:
                q.append((new_i, new_j))
                visited[state][new_i][new_j] = True
    return 1

N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(input()))
visited = {'R/G/B':[[False for _ in range(N)] for _ in range(N)], 'RG/B':[[False for _ in range(N)] for _ in range(N)]}
section = {'R/G/B':0, 'RG/B':0}
for i in range(N):
    for j in range(N):
        for state in ['R/G/B', 'RG/B']:
            section[state] += bfs((i,j),state)
print(*section.values())