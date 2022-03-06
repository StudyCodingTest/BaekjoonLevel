# 1,2,3 ADD
# 

import sys
input = sys.stdin.readline

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return solution(n-1) + solution(n-2) + solution(n-3)
    

for _ in range(int(input())):
    print(solution(int(input())))