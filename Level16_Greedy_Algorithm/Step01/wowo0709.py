# 동전 0
# 68ms
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
idx = len(coins)-1
cnt = 0
while K > 0:
    p,q = divmod(K,coins[idx])
    cnt += p
    K = q
    idx -= 1
    
print(cnt)
    