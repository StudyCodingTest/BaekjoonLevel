# 수 정렬하기 3
# 9536ms

import sys

count_sums = [0]*10001 

# Counting Sort
for i in range(int(sys.stdin.readline())) :
    count_sums[int(sys.stdin.readline())] += 1
for i in range(10001) :
    if count_sums[i] != 0 :
        for j in range(count_sums[i]):
            print(i)


