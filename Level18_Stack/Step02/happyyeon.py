# 제로
# 108ms

import sys
input = sys.stdin.readline

stack = [] # 스택 생성
for _ in range(int(input())) :
    num = int(input()) 

    if num == 0 :
        stack.pop()
    else :
        stack.append(num)

print(sum(stack))