# 쉬운 계단 수
# 76ms
N = int(input())
cnts = [[0]*10,[1]*10] + [[0 for _ in range(10)] for _ in range(N-1)]
for i in range(2,N+1):
    for j in range(10):
        if j == 0: cnts[i][j] = cnts[i-1][j+1]
        elif j == 9: cnts[i][j] = cnts[i-1][j-1]
        else: cnts[i][j] = (cnts[i-1][j-1]+cnts[i-1][j+1])%(10**9)
print(sum(cnts[N][1:])%(10**9))