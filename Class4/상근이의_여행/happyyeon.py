import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    vertex,edge = map(int,input().split())
    # 부모 테이블 초기화
    parent = [0]*(vertex+1)
    for i in range(1,vertex+1):
        parent[i] = i

    # find 연산
    def find_parent(parent,x):
        # x번의 부모노드가 x가 아니라 다른 노드다
        if parent[x] != x:
            # 그 다른 노드의 부모노드를 찾는 재귀
            parent[x] = find_parent(parent,parent[x])
        # x번의 부모노드가 x이다
        return parent[x]

    # union 연산
    def union_parent(parent,a,b):
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        # 노드 번호가 작은 것이 부모노드가 되도록 설정
        if a<b:
            parent[b] = a
        else:
            parent[a] = b

    # 간선 정보 담을 리스트, count =  신장 트리 총 간선 개수
    edges = []
    count = 0

    # 간선 정보
    for _ in range(edge):
        a,b = map(int,input().split())
        edges.append((a,b))

    # 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
    for i in range(edge):
        a,b = edges[i]

        # find 연산 후, 부모노드 다르면 사이클 발생하지 않으므로 union 연산 수행 --> 최소 신장 트리에 포함
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            count += 1
    print(count)