#문제: ACM 호텔, 시간: 80ms
import sys


test = int(input())
test_list = []
for _ in range(test):
    test_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(test):
    if test_list[i][2]%test_list[i][0] == 0:
        count = test_list[i][2]//test_list[i][0]
    else:
        count = test_list[i][2]//test_list[i][0] + 1
    Y = test_list[i][2]-test_list[i][0]*(count-1)
    print(Y*100+count)
