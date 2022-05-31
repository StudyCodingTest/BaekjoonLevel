import sys
from collections import deque
sys.stdin = open('input', 'r')
visited = []

n, m, v = map(int, input().split())
node = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a][b] = True
    node[b][a] = True


def DFS(v, visited):
    for dst in range(len(node[v])): # v 노드에서 갈 수 있는 간선을 저장해놓은 리스트
        if node[v][dst]: # 만약 갈 수 있다면 작은 정점부터
            if dst in visited: #이미 방문한 곳이라면 pass
                continue
            else:
                visited.append(dst) # 방문한다.
                v = dst #출발점 초기화
                DFS(v, visited) # 초기화된 출발점으로부터 다시 탐색 시작
    return visited


def BFS(v):
    q = deque()
    visited = [] # 방문목록 초기화
    visited.append(v) # 처음 출발점 visited 목록에 추가
    q.append(v) # 처음 출발점 queue에 추가
    while q:
        start = q.popleft() # 출발지 입력받음
        for dst in range(len(node[start])): # 현재 출발점에서 갈 수 있는곳 탐색
            if node[start][dst]: # 갈수 있다면,
                if dst in visited: # 방문한적 있는지 체크
                    continue # 이미 방문 --> pass
                else: # 아직 방문하지 X
                    visited.append(dst) # 방문 목록에 추가
                    q.append(dst) # queue에도 추가
    return visited


visited.append(v) # 처음에 바로 탐색하기위해 출발점 방문목록에 추가해줌
ans_dfs = DFS(v, visited)
ans_bfs = BFS(v)

for i in range(len(ans_dfs)):
    if i == len(ans_dfs) - 1:
        print(ans_dfs[i])
    else:
        print(ans_dfs[i], end=' ')

for i in range(len(ans_bfs)):
    if i == len(ans_bfs) - 1:
        print(ans_bfs[i])
    else:
        print(ans_bfs[i], end=' ')

# for i in ans_dfs:
#     print(i, end=' ')
# print()
# for i in ans_bfs:
#     print(i, end=' ')
