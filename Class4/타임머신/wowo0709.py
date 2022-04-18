import sys
input = sys.stdin.readline
INF = float('inf')
def bellman_ford(startV):
    c,c[startV] = [INF for _ in range(N+1)],0
    for it in range(N):              # 갱신 횟수 제한
        for cv in graph.keys():     # 각 정점에 대하여,
            if c[cv] == INF:         # 아직 방문한 적이 없으면 건너뛰기
	    continue
            for nc,nv in graph[cv]: # 최단거리 갱신
                tmp_c = c[cv] + nc
                if tmp_c < c[nv]:
                    c[nv] = tmp_c
                    if it >= N-1: return -1 # 최단 거리가 N번 이상 갱신된다면 음수 사이클에 갖힌 것 
    return c

N,M = map(int,input().split())
graph = {i+1:[] for i in range(N)}
for _ in range(M):
    A,B,C = map(int,input().split())
    graph[A].append((C,B)) # 방향 그래프
ans = bellman_ford(1)
if ans == -1: print(-1)
else: 
    for c in ans[2:]: print(c if c < INF else -1)