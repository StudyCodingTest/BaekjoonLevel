# 연산자 끼워넣기
# 1번 풀이: permutations 모듈 사용, 1412ms(PyPy3)
N = int(input())
nums = list(map(int, input().split()))
ops = []
cnt = list(map(int, input().split()))
for op, cnt in zip(['+','-','*','/'],cnt): ops += list(op*cnt)

from itertools import permutations as P
minnum, maxnum = float('inf'), -float('inf')
for case in P(ops, N-1):
    tmp = nums[0]
    for op, num in zip(case, nums[1:]):
        if op == '+': tmp += num
        elif op == '-': tmp -= num
        elif op == '*': tmp *= num
        elif op == '/': tmp = int(tmp/num)
    if tmp < minnum: minnum = tmp
    if maxnum < tmp: maxnum = tmp
print(maxnum, minnum, sep='\n') 



# 2번 풀이: 재귀 백트래킹, 248ms(PyPy3)
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

minnum, maxnum = float('inf'), -float('inf')
def result(now, idx):
    global minnum, maxnum
    if idx == N:
        maxnum = max(now, maxnum)
        minnum = min(now, minnum)
        return
    if ops[0] > 0:
        ops[0] -= 1
        result(now + nums[idx], idx+1)
        ops[0] += 1
    if ops[1] > 0:
        ops[1] -= 1
        result(now - nums[idx], idx+1)
        ops[1] += 1
    if ops[2] > 0:
        ops[2] -= 1
        result(now * nums[idx], idx+1)
        ops[2] += 1
    if ops[3] > 0:
        ops[3] -= 1
        result(int(now/ nums[idx]), idx+1)
        ops[3] += 1

result(nums[0], 1)
print(maxnum, minnum, sep='\n')
