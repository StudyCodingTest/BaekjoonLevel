# -*-coding:utf-8-*-
# 케빈 베이컨의 6단계 법칙
# 88ms
from collections import deque


def kevin(graph,start,n):
    # 초기화 작업
    kevin_nums = [0]*(n+1) # 각 사람에 대한 kevin num
    visited = [start] # 이미 방문한 노드
    queue = deque() # 다음 방문할 노드
    queue.append(start)

    while queue:
        current = queue.popleft()
        for i in graph[current]: # 아까 연결한 graph를 불러온다.
            if i not in visited:
                kevin_nums[i] = kevin_nums[current] + 1 # 원소에 해당하는 kevin_nums의 index를 +1 해준다.
                visited.append(i) # 해당 원소를 방문했음을 체크한다.
                queue.append(i) # 해당 원소를 다음 방문지 목록에 추가한다.
    return sum(kevin_nums)

import sys
input = sys.stdin.readline

# input
n,m = map(int,input().split())
# 그래프 초기화
graph = [[0]*(n+1) for _ in range(n+1)]

# 그래프 연결
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []
for i in range(1,n+1):
    answer.append(kevin(graph,i,n))

print(answer.index(min(answer))+1)


