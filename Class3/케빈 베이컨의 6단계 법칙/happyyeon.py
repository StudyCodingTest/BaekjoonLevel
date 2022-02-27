# -*-coding:utf-8-*-
# �ɺ� �������� 6�ܰ� ��Ģ
# 88ms
from collections import deque


def kevin(graph,start,n):
    # �ʱ�ȭ �۾�
    kevin_nums = [0]*(n+1) # �� ����� ���� kevin num
    visited = [start] # �̹� �湮�� ���
    queue = deque() # ���� �湮�� ���
    queue.append(start)

    while queue:
        current = queue.popleft()
        for i in graph[current]: # �Ʊ� ������ graph�� �ҷ��´�.
            if i not in visited:
                kevin_nums[i] = kevin_nums[current] + 1 # ���ҿ� �ش��ϴ� kevin_nums�� index�� +1 ���ش�.
                visited.append(i) # �ش� ���Ҹ� �湮������ üũ�Ѵ�.
                queue.append(i) # �ش� ���Ҹ� ���� �湮�� ��Ͽ� �߰��Ѵ�.
    return sum(kevin_nums)

import sys
input = sys.stdin.readline

# input
n,m = map(int,input().split())
# �׷��� �ʱ�ȭ
graph = [[0]*(n+1) for _ in range(n+1)]

# �׷��� ����
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = []
for i in range(1,n+1):
    answer.append(kevin(graph,i,n))

print(answer.index(min(answer))+1)


