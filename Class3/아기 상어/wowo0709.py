N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]

didj = [(-1,0),(1,0),(0,-1),(0,1)]
from collections import deque
def bfs(cur):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([(cur,0)]) # 위치, 거리
    visited[cur[0]][cur[1]] = True
    dist = float('inf')
    rets = []
    while q:
        ((ci,cj),d) = q.popleft()
        if 0 < MAP[ci][cj] < shark_size:
            dist = d
            rets.append(((ci,cj),d))
            continue
        for di,dj in didj:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and MAP[ni][nj] <= shark_size and not visited[ni][nj] and d < dist:
                q.append(((ni,nj),d+1))
                visited[ni][nj] = True
    rets.sort(key=lambda x:(x[1],x[0][0],x[0][1]))
    return rets[0] if rets else (None,None) 

shark_size, total_time, fish_to_be_bigger = 2, 0, 2
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            cur = (i,j)
            MAP[i][j] = 0
            break
while True:
    dest, dist = bfs(cur)
    if not dest:
        break
    MAP[dest[0]][dest[1]] = 0
    cur = dest
    total_time += dist
    fish_to_be_bigger -= 1
    if fish_to_be_bigger == 0:
        shark_size += 1
        fish_to_be_bigger = shark_size

print(total_time)


'''
시간초과
N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]

didj = [(-1,0),(1,0),(0,-1),(0,1)]
from collections import deque
def bfs(cur,dest):
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque([(cur,0)]) # 위치, 거리
    visited[cur[0]][cur[1]] = True
    dist = float('inf')
    while q:
        ((ci,cj),d) = q.popleft()
        if (ci,cj) == dest:
            dist = d
            break
        for di,dj in didj:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and MAP[ni][nj] <= shark_size and not visited[ni][nj]:
                q.append(((ni,nj),d+1))
                visited[ni][nj] = True
    return dist

shark_size, total_time, fish_to_be_bigger = 2, 0, 2
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            cur = (i,j)
            MAP[i][j] = 0
            break
while True:
    # 먹을 수 있는 물고기의 위치를 모두 찾는다. 
    dests = []
    for i in range(N):
        for j in range(N):
            dist = abs(cur[0]-i)+abs(cur[1]-j)
            if 0 < MAP[i][j] < shark_size:
                dests.append([(i,j),None]) #위치, 거리
    # 위에서 찾은 물고기들 중 가장 가까운 물고기를 찾는다. 
    for i in range(len(dests)):
        dests[i][1] = bfs(cur,dests[i][0])
    dests = sorted(dests,key=lambda x:x[1]) # 탐색 자체를 왼쪽->오른쪽, 위쪽->아래쪽으로 해서 문제 조건 만족
    if len(dests) == 0 or dests[0][1] == float('inf'):
        break
    dest, dist = dests[0]
    # 여러 정보들을 갱신한다. 
    MAP[dest[0]][dest[1]] = 0
    cur = dest
    total_time += dist
    fish_to_be_bigger -= 1
    if fish_to_be_bigger == 0:
        shark_size += 1
        fish_to_be_bigger = shark_size

print(total_time)
'''




