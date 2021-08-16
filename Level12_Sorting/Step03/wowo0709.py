# 수 정렬하기 3
# 8736ms (카운팅 정렬)
import sys
input = sys.stdin.readline
UPPER_LIMIT = 10000
cnts = [0 for _ in range(UPPER_LIMIT+1)]
for _ in range(int(input())): cnts[int(input())] += 1
for num in range(len(cnts)): 
    for _ in range(cnts[num]):
        print(num)