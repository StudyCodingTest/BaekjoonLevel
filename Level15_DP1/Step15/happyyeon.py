# 연속합
#

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums_minus = []
for num in nums :
    if num < 0 :
        nums_minus.append(num)
dp = []

# 전부 음수인 경우
if max(nums) < 0 :
    print(max(nums))
else :
    # 0 -> 음수
    if nums.index(nums_minus[0]) != 0 :
        dp.append(sum(nums[:nums.index(nums_minus[0])]))
    # 음수 -> 음수
    for i in range(1,len(nums_minus)) :
        dp.append(sum(nums[nums.index(nums_minus[i-1])+1:nums.index(nums_minus[i])]))
    # 음수 -> 끝
    if nums.index(nums_minus[-1]) != -1 :
        dp.append(sum(nums[nums.index(nums_minus[-1])+1:]))

    print(max(dp))