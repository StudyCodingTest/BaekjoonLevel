# 1197. 최소 스패닝 트리
import sys
input = sys.stdin.readline

# sol 1) kruskal (380ms)
def find(x):
    if parent[x] < 0:
        return x
    p = parent[x]
    root = find(p)
    return root
def union(x, y):
    px = find(x)
    py = find(y)
    if px == py:
        return False
    if parent[px] < parent[py]:
        parent[px] += parent[py]
        parent[py] = px
    else:
        parent[py] += parent[px]
        parent[px] = py
    return True
def kruskal(_edges):
    edges = sorted(_edges,key=lambda x:x[2])
    mst = set()
    total_weight = 0
    for u, v, w in edges:
        if union(u, v):
            mst.add((u,v))
            total_weight += w
        if len(mst) == V-1:
            break
    return total_weight

V, E = map(int, input().rstrip().split())
edges = [list(map(int,input().rstrip().split())) for _ in range(E)]
parent = [-1 for _ in range(V+1)]
print(kruskal(edges))

# sol 2) prim (500ms)
from heapq import heapify, heappush, heappop
def prim(graph, start):
    visited = [False for _ in range(V+1)]
    visited[start] = True
    heap = graph[start]
    heapify(heap)
    mst = set()
    total_weight = 0
    while heap:
        w, u, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.add((u,v))
        total_weight += w
        for nw, nu, nv in graph[v]: # v = nu
            if not visited[nv]:
                heappush(heap, (nw,nu,nv))
        if len(mst) == V-1:
            break
    return total_weight

V, E = map(int, input().rstrip().split())
graph = {i:[] for i in range(1,V+1)}
for _ in range(E):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((w,u,v))
    graph[v].append((w,v,u))
print(prim(graph, 1))