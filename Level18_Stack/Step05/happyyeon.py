# 스택 수열
# 160ms

import sys
input = sys.stdin.readline

n = int(input())
num_ascending = 0 # 스택에 들어갈 오름차순 숫자 1,2,3,...,n
stack = []
result = []

for i in range(n) :
    x = int(input())
    while num_ascending < x : 
        num_ascending += 1
        stack.append(num_ascending)
        result.append("+")
    if stack[-1] == x :
        stack.pop()
        result.append("-")
    else :
        print("NO")
        break

if not stack :
    print("\n".join(result))
