#-*- coding: utf-8 -*-
#요세푸스 문제 0
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
    for _ in range(k-1): # k-1 원소까지 원래 큐의 오른쪽에 붙인 후
        queue.append(queue.popleft())
    result.append(queue.popleft()) # k번째 원소를 결과 리스트에 저장한다.

print("<",end="")
print(*result,sep=", ",end="")
print(">")
