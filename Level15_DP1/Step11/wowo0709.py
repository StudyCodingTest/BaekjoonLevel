# 가장 긴 증가하는 부분 수열
# 176ms
lis = [1 for _ in range(int(input()))]
nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] < nums[j] and lis[i] >= lis[j]:
            lis[j] = lis[i]+1
print(max(lis))