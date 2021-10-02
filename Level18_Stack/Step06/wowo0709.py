# 오큰수
# 1540ms
ans = [-1 for _ in range(int(input()))]
nums = [(i,num) for i,num in enumerate(map(int, input().split()))]
s = [] # 값 저장
for num in nums:
    while s and s[-1][1] < num[1]:
        ans[s.pop()[0]] = num[1]
    s.append(num)

print(*ans)


# 1272ms
N = int(input())
nums = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
s = [] # 인덱스 저장
for i in range(N):
    while s and nums[s[-1]] < nums[i]:
        ans[s.pop()] = nums[i]
    s.append(i)

print(*ans)