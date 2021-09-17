# ATM
# 76ms
N, ts = int(input()), sorted(list(map(int,input().split())))
for i in range(1,N):
    ts[i] += ts[i-1]
print(sum(ts)) 