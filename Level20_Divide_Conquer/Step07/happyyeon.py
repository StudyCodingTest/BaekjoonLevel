# Matrix power
# 76ms
import sys
input = sys.stdin.readline

# initialize
n,b = map(int,input().split())
a= []
for _ in range(n):
    a.append(list(map(int,input().split())))

# matrix multiplication
def multiple_matrix(a,b):
    # matrix c: NxK matrix
    result = [[0]*n for _ in range(n)]

    # matrix multiplication
    for i in range(n):
        for j in range(n):
            for x in range(n):
                result[i][j] += a[i][x] * b[x][j]
    # problem condition
            result[i][j] %= 1000
    return result

# calculate mat^exp
def power_mat(mat,exp):
    if exp == 1: # mat^1 = mat
        return mat
    else:
        result = [[0 for _ in range(n)] for _ in range(n)]
        if exp%2 == 0 : # when exponent is even
            x = power_mat(mat,exp//2)
            result = multiple_matrix(x,x)
        else: # when exponent is odd -> mat^exp = mat^(exp-1)*mat
            x = power_mat(mat,exp-1)
            result = multiple_matrix(x,mat)
        
        return result

answer = power_mat(a,b)

for i in range(n):
    for j in range(n):
        print(answer[i][j]%1000, end=" ")
    print()