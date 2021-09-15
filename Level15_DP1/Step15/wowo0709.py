# 연속합
# 136ms
n = int(input())
nums = list(map(int, input().split()))
sums = [0 for _ in range(n)]
sums[0] = nums[0]
for i in range(1,n):
    sums[i] = max(nums[i],sums[i-1]+nums[i])
print(max(sums))