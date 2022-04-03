# 백준 1238 2트
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
# villages = {
#  마을 : [[다음 마을1, 시간], [다음 마을2, 시간], ...]]
# }

n,m,x = map(int,input().split())
villages = [[] for i in range(n+1)]

for i in range(m):
    village, next_village, time = map(int,input().split())
    villages[village].append([next_village,time])

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # (이전->현재) 걸린 시간, 현재 마을
        if dist > distance[now]: # distance = 출발 마을에서 index 마을까지 걸리는 최소 시간
            continue

        for i in villages[now]:
            cost = dist + i[1] # (이전->현재->다음) 걸릴 시간
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

# 마을 -> X 걸리는 최소 시간들
result1 = [0]

for i in range(1,n+1):
    distance = [INF]*(n+1)
    result1.append(dijkstra(i)[x])
# print(result1)
# X -> 마을 최소 시간들
result2 = [0]
distance = [INF]*(n+1)
result2 = dijkstra(x)
# print(result2)
# 마을 -> X -> 마을 최소 시간들
result3 = []

for i in range(1,n+1):
    result3.append(result1[i]+result2[i])
# print(result3)
# 그 중 최대 소요 시간
print(max(result3))
