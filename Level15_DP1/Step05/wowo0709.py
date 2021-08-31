# RGB 거리
# 132ms
costs = [0,0,0]
for n in range(int(input())):
    r,g,b = map(int, input().split())
    costs = [min(costs[1:])+r, min(costs[::2])+g, min(costs[:2])+b]
print(min(costs))