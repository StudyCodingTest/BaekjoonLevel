# 동전 0
# 68ms

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []
for _ in range(n) : # [1,5,10,...,5000,10000,50000]
    coins.append(int(input()))

counts_coin = [] # 동전 개수 저장해놓기
i = n-1
j = 0
while n!=0 and i!=-1 : # n=0 or 리스트 전체를 돌았으면 STOP
    if k//coins[i] != 0 :
        counts_coin.append(k//coins[i]) # N을 나눌 수 있는 동전들 중 제일 큰 값부터 챙김
        k -= counts_coin[j]*coins[i]
        i -= 1
        j += 1
    else :
        i -= 1
print(sum(counts_coin))