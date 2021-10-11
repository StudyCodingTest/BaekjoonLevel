# 회전하는 큐
# 88ms
from collections import deque
N, M = map(int, input().split())
idxs = list(map(int, input().split()))
nums = deque([i for i in range(1,N+1)])

cnt = 0
for idx in idxs:
    for i in range(len(nums)//2+1):
        if nums[i] == idx:
            nums.rotate(-i)
            cnt += i
            break
        elif nums[-(i+1)] == idx:
            nums.rotate(i+1)
            cnt += i+1
            break
    nums.popleft()

print(cnt)