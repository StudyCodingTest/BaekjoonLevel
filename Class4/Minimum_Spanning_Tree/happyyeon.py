import sys
input = sys.stdin.readline

vertex, edge = map(int,input().split())
edges = []
parent = [0]*(vertex+1)
#0. 모든 노드의 부모 노드를 자기 자신으로 초기화
for i in range(1,vertex+1):
    parent[i] = i
for i in range(edge):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

#1. 주어진 모든 간선 정보에 대해 간선 비용이 낮은 순서로 정렬
edges.sort()

# x의 부모 노드를 찾는 함수
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

# 간선을 연결해주는 함수
def union(parent,a,b):
    # a의 부모노드를 찾고 b의 부모노드를 찾아서 
    a = find(parent,a)
    b = find(parent,b)
    # 노드 번호가 작은것이 부모 노드가 되도록 설정
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

sum_cost = 0 # 최소 신장 트리 모든 간선 비용
#2. 정렬된 간선 정보를 하나씩 확인하면서 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인
for edge in edges:
    cost,a,b = edge
    
    #3. 만약 사이클이 발생하지 않은 경우, 최소 신장 트리에 포함시키고 사이클이 발생한 경우, 포함X
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        sum_cost += cost

print(sum_cost)