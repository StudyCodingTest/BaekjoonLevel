#-*- coding: utf-8 -*-
# µ¦
# 104ms
from collections import deque
import sys
input = sys.stdin.readline
queue = deque() # create queue 
for _ in range(int(input())):
    command = input().split() # input deque command
    if command[0] == "push_front": # push integer at front
        queue.appendleft(int(command[1]))
    elif command[0] == "push_back": # push integer at back
        queue.append(int(command[1]))
    elif command[0] == "pop_front":
        if not queue :
            print(-1)
        else :
            print(queue.popleft())
    elif command[0] == "pop_back":
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if not queue :
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    

