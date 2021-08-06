# 소수
# 80ms
M, N = int(input()), int(input())
isprime = [False, False] + [True for _ in range(N+1)]
for i in range(2,N+1):
    if not isprime[i]: continue
    for j in range(2*i, N+1, i):
        isprime[j] = False

ans = [num for num in range(M, N+1) if isprime[num]]
if ans: print(sum(ans), ans[0], sep='\n')
else: print(-1)
