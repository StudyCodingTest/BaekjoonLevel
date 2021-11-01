# 곱셈
# 68ms
def cal_power(n,k,c): # n^k%c
    if k in memo: pow = memo[k]
    elif k % 2 == 0: pow = cal_power(n,k//2,c) * cal_power(n,k//2,c)
    else: pow = cal_power(n,1,c) * cal_power(n,k-1,c)
    
    if k not in memo: memo[k] = pow % c
    return memo[k] % c

A, B, C = map(int,input().split())
memo = {0:1,1:A}
print(cal_power(A,B,C))