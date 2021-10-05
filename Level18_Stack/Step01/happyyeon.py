# 스택
# 136ms

import sys
input = sys.stdin.readline

stack = [] # 스택 리스트 생성
for _ in range(int(input())) :
    command = input().split() # stack command : list command
    len_stack = len(stack)
    if command[0] == "push" : # push : append
        stack.append(command[1])
    if command[0] == "pop" : # pop : pop
        if len_stack == 0 :
            print(-1)
        else :
            print(stack.pop())
    if command[0] == "size" : # size : len
        print(len_stack)
    if command[0] == "empty" : # empty : len
        if len_stack == 0 :
            print(1)
        else :
            print(0)
    if command[0] == "top" : # top : (index = -1)
        if len_stack == 0 :
            print(-1)
        else :
            print(stack[-1])
