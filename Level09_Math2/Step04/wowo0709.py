# 소수 구하기
# 396ms
M, N = map(int, input().split())
isprime = [False, False] + [True for _ in range(N+1)]
for i in range(2,int(N**(1/2))+1):
    if not isprime[i]: continue
    for j in range(2*i, N+1, i):
        isprime[j] = False

print(*[num for num in range(M, N+1) if isprime[num]], sep='\n')