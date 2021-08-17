# 수 정렬하기
# 120ms (모두 입력 후 정렬하기)
nums = []
for _ in range(int(input())): nums.append(int(input()))
print(*sorted(nums),sep='\n')

# 120ms (매 입력 시 정렬된 위치로 삽입하기)
from bisect import insort
nums = []
for _ in range(int(input())): insort(nums,int(input()))
print(*nums,sep='\n')