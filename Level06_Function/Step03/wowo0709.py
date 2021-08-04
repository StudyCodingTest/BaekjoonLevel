# 문제: 함수
# 시간: 68ms
def is_hansoo(n):
    nums = list(map(int,list(str(n))))
    for i in range(1,len(nums)-1):
        if nums[i] - nums[i-1] != nums[i+1] - nums[i]: return False
    else: return True

N = int(input())
answer = 0
for n in range(1,N+1): 
    answer += is_hansoo(n)
print(answer)