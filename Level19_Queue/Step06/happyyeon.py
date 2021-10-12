#-*- coding: utf-8 -*-
# 회전하는 큐
# 92ms

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # n개의 덱 원소 중에서 m개를 뽑는다고 할 때
queue = deque(range(1,n+1)) # 1~n 덱 생성
numbers = list(map(int,input().split())) # 뽑고자 하는 리스트
count = 0 # 2번과 3번의 연산 횟수
for i in range(m):
    if queue[0] == numbers[i]:
        queue.popleft()
        continue
    queue_idx = queue.index(numbers[i]) 
    if queue_idx >= len(queue)/2: #뽑으려고 하는 인덱스가 큐의 절반보다 뒤에 있으면 시계 방향 회전
        x = len(queue)-(queue_idx)
        queue.rotate(x)
        count += x
        queue.popleft()
    else: # 뽑으려고 하는 인덱스가 큐의 절반보다 앞에 있으면 반시계 방향 회전
        queue.rotate(-queue_idx)
        count += queue_idx
        queue.popleft()
print(count)
