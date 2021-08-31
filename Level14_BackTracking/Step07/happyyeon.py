# 연산자 끼워넣기
#

import sys
# 입력 조건
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
add, sub, mul, div = map(int,sys.stdin.readline().split())
# 경우의 수 리스트
answers = []
def solve(num,idx,add,sub,mul,div) :
    global answers
    if idx == n : # 출력 조건
        answers.append(num)
        return
    # 재귀
    if add > 0 :
        solve(num+nums[idx],idx+1,add-1,sub,mul,div)
    if sub > 0 :
        solve(num-nums[idx],idx+1,add,sub-1,mul,div)
    if mul > 0 :
        solve(num*nums[idx],idx+1,add,sub,mul-1,div)
    if div > 0 :
        solve(num//nums[idx],idx+1,add,sub,mul,div-1)
    
solve(nums[0],1,add,sub,mul,div)
print(max(answers), min(answers), sep="\n")



