#-*- coding: utf-8 -*-
#�似Ǫ�� ���� 0
# 128ms
from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
queue = deque()
result = []
# Q = [1,2,3,4,5,6,7]
for num in range(1,n+1):
    queue.append(num)

while queue :
    for _ in range(k-1): # k-1 ���ұ��� ���� ť�� �����ʿ� ���� ��
        queue.append(queue.popleft())
    result.append(queue.popleft()) # k��° ���Ҹ� ��� ����Ʈ�� �����Ѵ�.

print("<",end="")
print(*result,sep=", ",end="")
print(">")
