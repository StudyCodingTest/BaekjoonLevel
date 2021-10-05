# 오큰수
# 1892ms

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split())) # INPUT 수열 
answer = [-1]*n # 정답 NGE 수열
stack = [] # stack = [숫자, 인덱스]

for i in range(n) :
    while stack and (stack[-1][0] < nums[i]) :
        value, idx = stack.pop()
        answer[idx] = nums[i]
    stack.append([nums[i], i])

print(*answer)




