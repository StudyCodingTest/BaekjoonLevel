import sys
input = sys.stdin.readline

"""
Correct code
"""
n,m = map(int,input().split())
arr = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for i in arr:
    temp += i
    prefix_sum.append(temp)

for _ in range(m):
    start,end = map(int,input().split())
    print(prefix_sum[end]-prefix_sum[start-1])



"""
Time error code
"""
# # Input & Variables setting
# n,m = map(int,input().split())
# arr = list(map(int,input().split()))
# sum = 0

# # Using cumulative sum & Index slicing
# for _ in range(m):
#     start,end = map(int,input().split())
#     for i in range(start-1,end):
#         sum += arr[i]
#     print(sum)
#     sum = 0