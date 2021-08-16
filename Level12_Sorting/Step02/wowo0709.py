# 수 정렬하기 2
# 1284ms (모두 입력 후 정렬하기)
import sys
input = sys.stdin.readline
nums = []
for _ in range(int(input())): nums.append(int(input()))
print(*sorted(nums),sep='\n')

# # 시간초과 (매 입력 시 정렬된 위치로 삽입하기)
import sys
input = sys.stdin.readline
from bisect import insort
nums = []
for _ in range(int(input())): insort(nums,int(input()))
print(*nums,sep='\n')

# 2048ms (힙 정렬)
import sys
input = sys.stdin.readline
from heapq import heapify, heappop
nums = []
for _ in range(int(input())): nums.append(int(input()))
heapify(nums)
while nums: print(heappop(nums))