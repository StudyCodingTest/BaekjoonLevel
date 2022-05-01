import sys
input = sys.stdin.readline
INF = int(1e9)
node,edge = map(int,input().split())
dist = [INF]*(node+1)
edges = []

for i in range(edge):
    edges.append(list(map(int,input().split())))


def bellman_ford(start):
    dist[start] = 0 # 시작 노드 초기화

    # 노드 개수 만큼 라운드 반복
    for i in range(node):
        # 모든 간선 탐색
        for j in range(edge):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            # 비용 업데이트
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost
            
                # 음수 순환 체크
                if i == node-1:
                    return True
    
    return False

if bellman_ford(1) == True:
    print(-1)
else:
    for i in range(2,node+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
