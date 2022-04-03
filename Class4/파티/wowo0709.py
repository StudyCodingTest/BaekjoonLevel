import sys
input = sys.stdin.readline

from heapq import heappush, heappop
def dijkstra(start, end):
    times = [float('inf') for _ in range(N+1)]
    heap = [(0, start)] # 최소힙(시간, 정점)
    while heap:
        ct, cv = heappop(heap)
        if ct > times[cv]:
            continue
        for nv, nt in dir_graph[cv]:
            if ct + nt < times[nv]:
                times[nv] = ct + nt
                heappush(heap, (times[nv],nv))
    return times[end]

N, M, X = map(int, input().split())
dir_graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    u, v, t = map(int, input().split())
    dir_graph[u].append((v,t)) # 도착점, 소요시간
print(max([dijkstra(start,X)+dijkstra(X,start) for start in set(range(1,N+1))-{X}]))
