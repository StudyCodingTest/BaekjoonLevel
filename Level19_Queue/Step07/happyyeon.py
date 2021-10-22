#-*- coding: utf-8 -*-
# AC
#

import sys
from collections import deque
for _ in range(int(input())):
    command = input().rstrip()
    n = int(input())
    nums = deque(input()[1:-1].split(","))

    if n==0:
        nums = []

    count_reverse = 0
    for i in range(len(command)):
        if command[i] == "R": # 시간복잡도를 줄이기 위해 뒤집는 횟수가 홀수번일 때만 뒤집음
            count_reverse += 1
        elif command[i] == "D":
            if not nums:
                print("error")
                break
            else:
                if count_reverse%2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
    
    if nums:
        if count_reverse%2 ==0:
            print("["+",".join(list(nums))+"]")
        else:
            nums.reverse()
            print("["+",".join(list(nums))+"]")

