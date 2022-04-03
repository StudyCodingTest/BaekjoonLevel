# 백준 1167, 2트
# 트리의 지름을 구하는 공식
#1. 트리에서 노드 아무거나를 x로 잡는다
#2. x에서 가장 먼 노드 y를 잡는다.
#3. y에서 가장 먼 노드 z를 잡는다.
# 트리의 지름 = distance(y,z)

import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)] # [0번 노드의 키와 밸류, 1번 노드의 키와 밸류 ,...]

visited = [0]*(v+1)
count = 0
for _ in range(v): 
    idx = 0
    temp = deque(list(map(int,input().split()))) # 1 3 2 -1
    item = temp.popleft() # item = 1 and temp = [3 2 -1]
    
    while True:
        graph[item].append((temp[idx],temp[idx+1])) # graph = [[],[3,2],[],...]

        if temp[idx+2] == -1:
            break
        idx += 2

# start에서 각 노드들까지의 거리들
def dfs(start,result):
    for e,d in graph[start]:
        if result[e] == 0:
            result[e] = result[start] + d
            dfs(e,result)

#1. 트리에서 노드 아무거나를 x로 잡는다
result1 = [0]*(v+1)
dfs(1,result1)
result1[1] = 0 # 이거 안 해주면 1 -> 1로 가는 값이 0이 아니게 됨
max_distance_node_y = result1.index(max(result1))

#2. x에서 가장 먼 노드 y를 잡는다.
result2 = [0]*(v+1)
dfs(max_distance_node_y,result2)
result2[max_distance_node_y] = 0
#3. y에서 가장 먼 노드 z를 잡는다.
# 트리의 지름 = distance(y,z)
print(max(result2))




