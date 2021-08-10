#문제: Fly me to the Alpha Centauri
#번호: 1011
#시간:

import sys
import math

testcase = int(input())
test = []
for _ in range(testcase):
    start, arrive = map(int, sys.stdin.readline().split())
    test.append([start, arrive])
for i in range(testcase):
    distance = test[i][1] - test[i][0]
    count = 0
    ans = 0
    move = 1
    cnt = 0
    flag = 0
    for _ in range(distance):
        count += 1
        cnt += 1
        if count == distance:
            ans += 1
            break
        if cnt == 2:
            cnt = 0
            flag = 1
        for _ in range(ans):
            if count == distance:
                break
            count += 1
    print(ans)






