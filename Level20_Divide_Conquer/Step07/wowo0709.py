# 행렬 제곱
# 72ms
def cal_matrix_mul(A, B): # A*B
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % 1000
    return C

def cal_matrix_power(A, b): # A^b
    if b in memo: X, Y = memo[b], I
    elif b % 2 == 0: X = Y = cal_matrix_power(A, b//2)
    else: X, Y = cal_matrix_power(A, b-1), A

    if b == 1 or b not in memo: memo[b] = cal_matrix_mul(X, Y)
    return memo[b]

n, b = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(n)]
I = [[0]*k + [1] + [0]*(len(A)-k-1) for k in range(len(A))] # 항등 행렬
memo = {1: A}
res = cal_matrix_power(A, b)
print(*[" ".join(map(str,r)) for r in res],sep='\n')