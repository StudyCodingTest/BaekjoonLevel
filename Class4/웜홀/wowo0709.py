# 1865. 웜홀
import sys
input = sys.stdin.readline

def bellman_ford(start):
    # times = [float('inf') for _ in range(N+1)]
    times = [10001 for _ in range(N+1)]
    times[start] = 0
    for i in range(N):
        for u in range(1, N+1):
            # if times[u] == 10001: continue
            for v, t in graph[u].items():
                if times[v] > times[u] + t:
                    times[v] = times[u] + t
                    if i == N-1: # N번째에도 갱신이 된다면 음수사이클 존재
                        return 'YES'
    return 'NO'

for tc in range(int(input())):
    N, M, W = map(int, input().rstrip().split())
    graph = {i:dict() for i in range(1,N+1)} # node: {adj_node:time, ...}
    for _ in range(M):
        s, e, t = map(int, input().rstrip().split())
        if e not in graph[s] or t < graph[s][e]:
            graph[s][e] = t
            graph[e][s] = t
    for _ in range(W):
        s, e, t = map(int, input().rstrip().split())
        graph[s][e] = -t
    print(bellman_ford(1))