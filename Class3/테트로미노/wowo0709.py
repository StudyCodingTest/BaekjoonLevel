'''
안 1. blocks_2x4와 blocks_4x2를 만들어 8개 수 중 4개의 수를 제외(단, 가능한 경우여야 함)해서 최대가 되는 값 탐색
blocks_2x4
1 2 3 4
5 6 7 8
blocks_4x2
1 2
3 4
5 6
7 8

안 2. 그래프 -> 각 노드마다(bruteforce) 4개의 블록을 bfs로 greedy하게 최대가 되도록 탐색
다익스트라 -> 가중치(여기서는 블록에 적힌 수)가 최대가 되도록 탐색
근거: MAP, 최대값 탐색, 노드 간 탐색

안 3. 안 2가 '틀렸습니다'
오답 경우 -> 6 6 이라서 한 쪽을 골랐는데 다른 쪽이 최대일 경우 (이 문제는 greedy하지 않음!!)
수정 -> 4개 탐색으로 가능한 모든 경우(dfs, backtracking) 중 최대 값

안 4. 일반적인 dfs로는 탐색하지 못 하는 테트로미노 형태가 있음 -> 어떻게??
'''

# 안 4
N, M = map(int, input().split()) # 세로, 가로
MAP = [list(map(int, input().split())) for _ in range(N)]
MAP_maxval = max(map(max,MAP))

didj = [(-1,0),(1,0),(0,-1),(0,1)]
def backtracking(i,j,n,total):
    global ans
    if ans >= total + MAP_maxval*(4-n): # 가지치기 (안할 시: 시간초과 -> max_total과 비교 시: 6276ms -> ans와 비교 시: 336ms)
        return
    if n == 4: # 완료조건
        ans = max(ans,total)
        return
    for di, dj in didj: 
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if n == 2: # T 모양 탐색
                visited[ni][nj] = True
                backtracking(i,j,n+1,total+MAP[ni][nj])
                visited[ni][nj] = False
            visited[ni][nj] = True
            backtracking(ni,nj,n+1,total+MAP[ni][nj])
            visited[ni][nj] = False
    return

ans = 0
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        backtracking(i,j,1,MAP[i][j])
        visited[i][j] = False
print(ans)


# 안 2
# from heapq import heappop, heappush
# didj = [(-1,0),(1,0),(0,-1),(0,1)]
# def dijkstra(i,j):
#     heap = [(-MAP[i][j],(i,j))] # -1 * 블록에 적힌 수(최대힙), 블록 좌표, path 길이
#     visited = set() # 4개만 탐색하니 방문한 좌표를 넣는 식으로 구현(메모리 절약)
#     ret = 0
#     for _ in range(4):
#         val, (ci,cj) = heappop(heap)
#         ret += -val
#         visited.add((ci,cj))
#         for di, dj in didj:
#             ni, nj = ci+di, cj+dj
#             if 0 <= ni < N and 0 <= nj < M and (ni,nj) not in visited:
#                 heappush(heap, (-MAP[ni][nj],(ni,nj)))
#     return ret

# ans = 0
# for i in range(N):
#     for j in range(M):
#         ans = max(ans,dijkstra(i,j))
# print(ans)

# 안 3
# didj = [(-1,0),(1,0),(0,-1),(0,1)]
# def backtracking(i,j,n,max_total,total):
#     if n == 4: # 완료조건
#         return max(max_total,total)
#     for di, dj in didj: 
#         ni, nj = i+di, j+dj
#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
#             visited[ni][nj] = True
#             max_total = backtracking(ni,nj,n+1,max_total,total+MAP[ni][nj])
#             visited[ni][nj] = False
#     return max_total

# ans = 0
# visited = [[False for _ in range(M)] for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         visited[i][j] = True
#         ans = max(ans,backtracking(i,j,1,0,MAP[i][j]))
#         visited[i][j] = False
# print(ans)