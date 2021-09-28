# 이항 계수 2
# 72ms
N, K = map(int, input().split())
fact = [1 for _ in range(N+1)]
for i in range(2,N+1): fact[i] = i * fact[i-1]
print(fact[N]//(fact[N-K]*fact[K]) % 10007)