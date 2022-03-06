# -*-coding:utf-8 -*-
# 이중 우선순위 큐
# 8324ms

import heapq
import sys

input = sys.stdin.readline

def sync(heap):
    while heap and not is_valid[heap[0][1]]:
        heapq.heappop(heap)

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    k = int(input())
    is_valid = [False]*k
    for i in range(k):
        operator, num = input().split()
        num = int(num)
        if operator == 'I':
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-1*num,i))
            is_valid[i] = True
        elif operator == 'D':
            if num == 1:
                sync(max_heap)
               
                if max_heap:
                    is_valid[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    
            if num == -1:
                sync(min_heap)

                if min_heap:
                    is_valid[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    sync(min_heap)
    sync(max_heap)

    if min_heap and max_heap:
        print(-1*max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

# 시간초과 코드
# for _ in range(int(input())):
#     q = deque()
#     for _ in range(int(input())):
#         operator, num = input().split()
#         num = int(num)
#         if operator == 'I':
#             q.append(num)
#         elif operator == 'D':
#             if not q:
#                 continue
#             if num == 1:
#                 q.remove(max(q))
#             if num == -1:
#                 q.remove(min(q))
    
#     if q:
#         print(max(q),min(q))
#     else:
#         print("EMPTY")


