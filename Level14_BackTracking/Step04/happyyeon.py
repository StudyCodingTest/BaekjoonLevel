# N과 M(4)
# 128ms

import sys

n,m = map(int,sys.stdin.readline().split()) # N과 M을 입력 받음

nums = [] # 결과를 출력할 배열

def backtrack():
    if len(nums) == m : # 배열이 다 차면 POP(DFS 종료)
        print(" ".join(str(num) for num in nums)) 
    
    for num in range(1, n+1) :
        if len(nums) == m or (len(nums) >= 1 and max(nums) > num) : # 만약 그 숫자가 이미 있으면 제외 (가지치기)
            continue
        nums.append(num) # 만약 그 숫자가 없으면 추가
        backtrack() # 깊이 우선 탐색(DFS)
        nums.pop() # 다음 순열 출력을 위하여 리스트를 비워준다.

backtrack()