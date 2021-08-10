# 네번째 점
# 108ms
from collections import Counter
xs, ys = [], []
for _ in range(3):
    x, y = input().split()
    xs.append(x)
    ys.append(y)
for coors in [xs,ys]: 
    print(Counter(coors).most_common()[1][0], end=' ')