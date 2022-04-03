# 백준 1167 , 1트

import sys
from collections import deque
input = sys.stdin.readline

v = int(input()) #5
graph = [[] for _ in range(v+1)] # [0번 노드의 키와 밸류, 1번 노드의 키와 밸류 ,...]

visited = [0]*(v+1)
count = 0
candidate_list = [[] for _ in range(v+1)]
for _ in range(v): 
    idx = 0
    temp = deque(list(map(int,input().split()))) # 1 3 2 -1
    item = temp.popleft() # item = 1 and temp = [3 2 -1]
    
    while True:
        graph[item].append((temp[idx],temp[idx+1])) # graph = [[],[3,2],[],...]

        if temp[idx+2] == -1:
            break
        idx += 2
# 최종 그래프 = [[],[(3,2)],[(4,4)],[(1,2),(4,3)],[(2,4),(3,3),(5,6)],...]

def dfs(item): # item = 1
    count = 0
    visited[item] = 1 # 1번 노드 방문 체크
    for i in range(len(graph[item])):
        next_item = graph[item][i][0] # 3
        distance = graph[item][i][1] # 2

        if not visited[next_item]: # 3번 노드 방문한 적 없음
            count += distance # 1번의 총 거리에 +2
            dfs(next_item) # dfs(3)
    candidate_list[item].append(count)

max_value = 0

for i in range(1,v+1):
    dfs(i)
    max_value = max(max(candidate_list[i]),max_value)

print(max_value)



