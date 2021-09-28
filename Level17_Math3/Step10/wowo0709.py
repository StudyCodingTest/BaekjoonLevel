# 패션왕 신해빈
# 128ms
from functools import reduce

for t in range(int(input())):
    costums = dict()
    for _ in range(int(input())):
        name, costum = input().split()
        costums[costum] = costums.get(costum,1) + 1
    print(reduce(lambda x, y: x * y, costums.values(), 1) - 1)