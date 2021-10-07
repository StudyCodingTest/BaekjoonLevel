# 요세푸스 문제 0
# 100ms
from collections import deque
N, K = map(int, input().split())
nums = deque([str(num) for num in range(1,N+1)])
ans = []
while nums:
    nums.rotate(-(K-1))
    ans.append(nums.popleft())

print('<'+", ".join(ans)+'>')