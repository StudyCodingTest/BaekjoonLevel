# Biggest rectangular in histogram
# 512ms

from collections import deque
import sys
input = sys.stdin.readline

while True:
    rec = list(map(int,input().split()))
    n = rec.pop(0)

    if n==0:
        break
    
    stack = deque()
    answer = 0

    # find left first in turn
    for i in range(n):
        # if appending element height smaller than last element in stack
        # --> pop elements and calculate maximum rectangular area
        while len(stack) != 0 and rec[i] < rec[stack[-1]]:
            temp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer,width*rec[temp])
        stack.append(i)
    
    # process remainder in stack
    while len(stack) != 0:
        temp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer,width*rec[temp])
    
    print(answer)