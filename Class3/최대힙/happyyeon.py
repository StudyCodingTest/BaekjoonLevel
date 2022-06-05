import sys
import heapq
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    num = int(input())

    if num:
        heapq.heappush(heap,-num)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-1*heapq.heappop(heap))
