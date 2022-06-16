import sys
input = sys.stdin.readline
N, M = int(input()), int(input())
dir_graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    dir_graph[u].append((w,v))
start, end = map(int, input().rstrip().split())

from heapq import heappush, heappop
costs = [float('inf') for _ in range(N+1)]
heap = [(0, start)]
while heap:
    cost, node = heappop(heap)
    if cost > costs[node]:
        continue
    for weight, adj_node in dir_graph[node]:
        if cost+weight < costs[adj_node]:
            costs[adj_node] = cost+weight
            heappush(heap, (cost+weight, adj_node))
print(costs[end])