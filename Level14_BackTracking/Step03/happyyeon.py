# N과 M(3)
# 2744ms

import sys

n,m = map(int,sys.stdin.readline().split()) # N과 M을 입력 받음

sys.setrecursionlimit(10 ** 6)

nums = [] # 결과를 출력할 배열

def backtrack():
    if len(nums) == m : # 배열이 다 차면 POP(DFS 종료)
        print(" ".join(str(num) for num in nums)) 
    
    for num in range(1, n+1) :
        if len(nums) == m :
            continue
        nums.append(num) # 만약 그 숫자가 없으면 추가
        backtrack() # 깊이 우선 탐색(DFS)
        nums.pop() # 다음 순열 출력을 위하여 리스트를 비워준다.

backtrack()