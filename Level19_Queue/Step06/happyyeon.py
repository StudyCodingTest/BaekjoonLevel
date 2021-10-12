#-*- coding: utf-8 -*-
# ȸ���ϴ� ť
# 92ms

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) # n���� �� ���� �߿��� m���� �̴´ٰ� �� ��
queue = deque(range(1,n+1)) # 1~n �� ����
numbers = list(map(int,input().split())) # �̰��� �ϴ� ����Ʈ
count = 0 # 2���� 3���� ���� Ƚ��
for i in range(m):
    if queue[0] == numbers[i]:
        queue.popleft()
        continue
    queue_idx = queue.index(numbers[i]) 
    if queue_idx >= len(queue)/2: #�������� �ϴ� �ε����� ť�� ���ݺ��� �ڿ� ������ �ð� ���� ȸ��
        x = len(queue)-(queue_idx)
        queue.rotate(x)
        count += x
        queue.popleft()
    else: # �������� �ϴ� �ε����� ť�� ���ݺ��� �տ� ������ �ݽð� ���� ȸ��
        queue.rotate(-queue_idx)
        count += queue_idx
        queue.popleft()
print(count)
