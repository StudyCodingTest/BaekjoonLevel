# 통계학
# 684ms

import sys
from collections import Counter

nums = []

for i in range(int(sys.stdin.readline())) :
    nums.append(int(sys.stdin.readline()))
nums.sort() # 최빈값을 가장 작은 순으로 2개 추리기 위하여
mode = Counter(nums).most_common(2) # 가장 많이 나타난 2개
print(round(sum(nums)/len(nums))) # 산술평균
print(nums[len(nums)//2]) # 중간값
print(mode[1][0] if len(mode) > 1 and mode[0][1] == mode[1][1] else mode[0][0]) # 최빈값
print(max(nums) - min(nums)) # 범위 



# import sys
# import numpy as np
# from collections import Counter

# nums = []

# for i in range(int(sys.stdin.readline())) :
#     nums.append(int(sys.stdin.readline()))
# nums.sort() # 최빈값을 가장 작은 순으로 2개 추리기 위하여
# mode = Counter(nums).most_common(2) # 가장 많이 나타난 2개
# print(round(np.mean(nums))) # 산술평균
# print(int(np.median(nums))) # 중간값
# print(mode[1][0] if len(mode) > 1 and mode[0][1] == mode[1][1] else mode[0][0]) # 최빈값
# print(max(nums) - min(nums)) # 범위 