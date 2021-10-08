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



'''
from collections import deque
N, M = map(int, input().split())
mask = deque([0 for _ in range(N)])
for idx in list(map(int, input().split())): mask[idx-1] = 1

cnt = 0
for _ in range(M): # 모든 idx를 pop할 때까지
    for i in range(N//2+1): # 양쪽에서 탐색
        if mask[i] == 1:
            mask.rotate(-i)
            cnt += i
            break
        elif mask[-(i+1)] == 1:
            mask.rotate(i+1)
            cnt += i+1
            break

    mask.popleft()

print(cnt)
'''

