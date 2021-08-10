#문제: 터렛
#번호: 1002
#시간: 72ms

import sys


testcase = int(input())
test = []
for _ in range(testcase):
    case = list(map(int, sys.stdin.readline().split()))
    test.append(case)

for i in range(testcase):
    r1 = test[i][2]
    r2 = test[i][5]
    x1, y1, x2, y2 = test[i][0], test[i][1], test[i][3], test[i][4]
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if x1 == x2 and y1 == y2: # 관측점이 같은 경우
        if r1 == r2: #관측점이 같고 거리도 같은 경우
            print(-1)
        else: #관측점이 같지만 거리가 다른 경우
            print(0)

    elif distance == r1 + r2 or distance + min(r1, r2) == max(r1, r2): # 한개의 점에서 외접하는 경우
        print(1)
    elif distance > r1 + r2 or distance + min(r1, r2) < max(r1, r2): # 멀어서 접점이 없는 경우
        print(0)
    else:
        print(2)
