import sys
input = sys.stdin.readline # 없으면 시간초과

N, M = map(int, input().split())
nums = [0] + list(map(int, input().rstrip().split()))
sums = [0 for _ in range(N+1)]
for i in range(1,N+1):
    sums[i] = nums[i] + sums[i-1]
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(sums[j]-sums[i-1])