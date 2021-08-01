# 문제: 나머지
# 시간: 72ms
import sys
input = sys.stdin.readline

nums = [0 for _ in range(42)]
for _ in range(10):
    nums[int(input())%42] = True

print(sum(nums))