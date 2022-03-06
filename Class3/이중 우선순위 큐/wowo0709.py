from heapq import heappush, heappop
import sys
input = sys.stdin.readline

for t in range(int(input())):
    k = int(input())
    max_heap, min_heap = [], []
    exists = [False for _ in range(k)] # idx번째 명령어로 삽입된 수가 존재하는지 여부
    for idx in range(k):
        cmd, n = input().rstrip().split()
        if cmd == 'I':
            heappush(min_heap, (int(n), idx))
            heappush(max_heap, (-int(n), idx))
            exists[idx] = True
        elif cmd == 'D':
            if n == '1':
                while max_heap and not exists[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap: 
                    exists[heappop(max_heap)[1]] = False
            elif n == '-1':
                while min_heap and not exists[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap: 
                    exists[heappop(min_heap)[1]] = False

    while max_heap and not exists[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not exists[min_heap[0][1]]:
        heappop(min_heap)
    if not max_heap or not min_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])