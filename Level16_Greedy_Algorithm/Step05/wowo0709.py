# 주유소
# 168ms
N = int(input())
dists = list(map(int,input().split()))
costs = list(map(int,input().split()))

loc, cost = 0, 0
for i in range(N):
    if costs[loc] > costs[i] or i == N-1:
        cost += costs[loc] * sum(dists[loc:i])
        loc = i
print(cost)