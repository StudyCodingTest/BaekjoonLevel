# 문제: 최댓값
# 시간: 72ms
import sys
input = sys.stdin.readline

nums = []
for i in range(1,10): 
    nums.append(int(input()))

maxnum = max(nums)
print(maxnum,nums.index(maxnum)+1)