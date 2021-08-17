# 블랙잭
# 112ms
N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for i in range(len(cards)-2):
    for j in range(i+1,len(cards)-1):
        for k in range(j+1,len(cards)):
            if ans < cards[i]+cards[j]+cards[k] <= M:
                ans = cards[i]+cards[j]+cards[k]

print(ans)