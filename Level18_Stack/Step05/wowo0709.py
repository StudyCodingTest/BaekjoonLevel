# 스택 수열
# 220ms
import sys
N = int(input())
obj = list(reversed([int(sys.stdin.readline()) for _ in range(N)]))
s = []
ans = []
for n in range(1,N+1):
    s.append(n)
    ans.append('+')
    while s and s[-1] == obj[-1]:
        s.pop()
        ans.append('-')
        obj.pop()

if len(obj) == 0: print(*ans, sep='\n')
else: print('NO')


    