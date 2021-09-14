# 전깃줄
# 76ms
N = int(input())
cords = sorted([list(map(int,input().split())) for _ in range(N)])
lis = [1 for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        if cords[i][1] < cords[j][1] and lis[i] >= lis[j]:
            lis[j] = lis[i]+1
print(N-max(lis))