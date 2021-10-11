# 프린터 큐
# 100ms
from collections import deque
for tc in range(int(input())):
    N, M = map(int, input().split())
    find_list = deque([0]*M + [1] + [0]*(N-M-1))
    priorities = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        max_idx = priorities.index(max(priorities))
        priorities.rotate(-max_idx)
        find_list.rotate(-max_idx)
        if find_list[0] == 1:
            print(cnt)
            break
        priorities.popleft()
        find_list.popleft()
        cnt += 1