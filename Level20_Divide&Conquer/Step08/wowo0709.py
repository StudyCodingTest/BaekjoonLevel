# 피보나치 수 6
# 68ms
'''
피보나치의 수열을 분할 정복으로 빨리 풀려면 행렬의 거듭제곱을 이용하면 된다. 
[[Fn+1,Fn],[Fn,Fn-1]] = [[F2,F1],[F1,F0]]^n = [[1,1],[1,0]]^n
'''
def cal_matrix_mul(A, B): # A*B
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % div
    return C

def cal_matrix_power(A, b): # A^b
    if b in memo: X, Y = memo[b], I
    elif b % 2 == 0: X = Y = cal_matrix_power(A, b//2)
    else: X, Y = cal_matrix_power(A, b-1), A

    if b == 1 or b not in memo: memo[b] = cal_matrix_mul(X, Y)
    return memo[b]

n, div = int(input()), int(1e+9) + 7
F = [[1,1],[1,0]] # 기본 피보나치 행렬
I = [[0]*k + [1] + [0]*(len(F)-k-1) for k in range(len(F))] # 항등 행렬
memo = {1: F}
res = cal_matrix_power(F, n)
print(res[0][1] if n >= 2 else 1)