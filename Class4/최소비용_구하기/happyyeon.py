import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# 초기 조건
city = int(input())
bus = int(input())
# 도시 --> 그래프로 표현
cities = [[] for _ in range(city+1)]
for i in range(bus):
    a,b,c = map(int,input().split())
    cities[a].append([b,c])
start,end = map(int,input().split()) # 출발지, 도착지

# "출발 노드 --> 각 노드" 최소 비용
distance = [INF]*(city+1)

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # (이전->현재) 걸린 시간, 현재 마을
        if dist > distance[now]: # distance = 출발 마을에서 index 마을까지 걸리는 최소 시간
            continue

        for i in cities[now]:
            cost = dist + i[1] # (이전->현재->다음) 걸릴 시간
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

# 정답 구하기
answer_list = dijkstra(start)
print(answer_list[end])