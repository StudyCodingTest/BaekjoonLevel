# 숨바꼭질 2
N, K = map(int, input().split())

from collections import deque
q = deque([(0,N)]) # time, cur
times = [float('inf') for _ in range(100001)]
ans_time, ans_cnt = float('inf'), 0
while q:
    time, cur = q.popleft()
    if time > ans_time:
        break
    if cur == K:
        if time == ans_time:
            ans_cnt += 1
        elif time < ans_time:
            ans_time = time
            ans_cnt = 1
        continue
    for next_cur in [cur+1, cur-1, cur*2]:
        if 0 <= next_cur <= 100000 and time+1 <= times[next_cur]:
            q.append((time+1, next_cur))
            times[next_cur] = time+1

print(ans_time, ans_cnt, sep='\n')