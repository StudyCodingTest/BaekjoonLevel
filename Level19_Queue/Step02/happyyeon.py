#-*- coding: utf-8 -*-
# 카드2
# 272ms
from collections import deque
import sys
input = sys.stdin.readline
queue = deque()
# 1~n까지 리스트에 추가
for num in range(1,int(input())+1) :
    queue.append(num)

while True :
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())