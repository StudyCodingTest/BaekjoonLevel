# 2638. 치즈
from collections import deque
didj = [(-1,0),(1,0),(0,-1),(0,1)]
def bfs(MAP: list, start: tuple):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([start])
    visited[start[0]][start[1]] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in didj:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M:
                if MAP[ni][nj] == 0 and visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = 1
                if MAP[ni][nj] == 1:
                    visited[ni][nj] += 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                MAP[i][j] = 0
    return MAP        

N, M = map(int, input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
GONE = [[0 for _ in range(M)] for _ in range(N)]
t = 0
while MAP != GONE:
    MAP = bfs(MAP,(0,0))
    t += 1
print(t)