# 소수 찾기
# 76ms
n = int(input())
nums = list(map(int, input().split()))
maxnum = max(nums)
# 에라토스테네스의 체
isPrime = [False, False] + [True]*(maxnum-1)
for i in range(2, maxnum+1):
    if isPrime[i]:
        for j in range(2*i, maxnum+1, i):
            isPrime[j] = False

print(sum([isPrime[num] for num in nums]))