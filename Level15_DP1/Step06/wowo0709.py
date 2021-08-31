# 정수 삼각형
# 208ms
nums = [[0]]
for i in range(1,int(input())+1):
    nums.append(list(map(int, input().split())))
    for j in range(i):
        if j == 0: nums[i][j] += nums[i-1][j]
        elif j == i: nums[i][j] += nums[i-1][j-1]
        else: nums[i][j] += max(nums[i-1][j-1:j+1])
print(max(nums[-1]))