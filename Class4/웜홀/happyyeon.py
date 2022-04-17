import sys
input = sys.stdin.readline
INF = int(1e9)

for _ in range(int(input())):
    num_node, num_edge, num_hall = map(int,input().split())
    edges = []
    dist = [INF]*(num_node+1)
    for _ in range(num_edge):
        a,b,c = map(int,input().split()) # a->b로 가는데 c시간
        edges.append([a,b,c])
        edges.append([b,a,c]) # 도로는 양방향이기 때문
    for _ in range(num_hall): # 웜홀은 단방향
        a,b,c = map(int,input().split())
        edges.append([a,b,-c])

    # 벨만 포드 알고리즘
    def bellman_ford(start):
        dist[start] = 0 # 시작 노드 초기화
        # 전체 노드 수만큼의 라운드 반복
        for i in range(num_node):
            # 매 반복마다 모든 간선 확인
            for j in range(2*num_edge+num_hall):
                cur = edges[j][0]
                next_node = edges[j][1]
                cost = edges[j][2]

                # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                # dist[cur] != INF 조건을 제함.
                if dist[next_node] > dist[cur] + cost:
                    dist[next_node] = dist[cur] + cost
                    # 마지막 라운드에서도 값이 갱신된다면 음수 순환 존재
                    if i == num_node-1:
                        return True
        
        return False
    
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")
