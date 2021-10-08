# AC
# 276ms
from collections import deque
for tc in range(int(input())):
    cmds = input().replace("RR","")
    N = int(input())
    nums = deque(list(input()[1:-1].split(',')))
    direct = 1 # 1: 앞, -1: 뒤
    for cmd in cmds:
        if cmd == 'R': direct = -direct
        elif cmd == 'D':
            if len(nums) == 0 or nums[0] == '': # 크기가 0
                print('error')
                break
            if direct == 1: nums.popleft()
            elif direct == -1: nums.pop()
    else: # error가 아닌 경우
        if direct == 1: print('['+",".join(nums)+"]")
        elif direct == -1: print('['+",".join(reversed(nums))+"]")