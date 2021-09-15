# 가장 긴 바이토닉 부분 수열
# 348ms
lis = [[1,1] for _ in range(int(input()))]
nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] < nums[j] and lis[i][0] >= lis[j][0]:
            lis[j][0] = lis[i][0]+1
for i in range(len(nums)-1,-1,-1):
    for j in range(i,-1,-1):
        if nums[i] < nums[j] and lis[i][1] >= lis[j][1]:
            lis[j][1] = lis[i][1]+1

print(max(map(sum,lis))-1)