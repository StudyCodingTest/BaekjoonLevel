# 통계학
# 500ms
import sys
input = sys.stdin.readline
nums = []
N = int(input())
for _ in range(N): nums.append(int(input()))
nums.sort()
# 산술평균
print(round(sum(nums)/N))
# 중앙값
print(nums[(N-1)//2])
# 최빈값
from collections import Counter
cnts = Counter(nums).most_common()
if len(cnts) > 1 and cnts[0][1] == cnts[1][1]: # 최빈값이 2개 이상이면,
    cnts.sort(key=lambda x:x[0], reverse=True)
    cnts.sort(key=lambda x:x[1])
    print(cnts[-2][0])
else:
    print(cnts[0][0])
# 범위
print(nums[-1]-nums[0])