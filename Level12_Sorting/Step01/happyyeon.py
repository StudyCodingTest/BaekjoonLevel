# 수 정렬하기
# 80ms

import sys

num_count = int(sys.stdin.readline())

arr = [0 for i in range(num_count)]

for i in range(num_count) :
    arr[i] = int(sys.stdin.readline())

arr.sort()

for num in arr :
    print(num)