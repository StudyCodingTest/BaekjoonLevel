# Fibonacci number 6
# 72ms

# initialize
n = int(input())
p=1000000007
base = [[1,1], [1,0]]

# A^n = [[Fn+1 Fn], [Fn Fn-1]]
# for calculation a power n 
# matrix multiplication
def multiple_matrix(a,b):
    # matrix c: NxK matrix
    result = [[0]*2 for _ in range(2)]

    # matrix multiplication
    for i in range(2):
        for j in range(2):
            for x in range(2):
                result[i][j] += a[i][x] * b[x][j]
    # problem condition
            result[i][j] %= p
    return result

# calculate mat^exp
def power_mat(mat,exp):
    if exp == 1: # mat^1 = mat
        return mat
    else:
        result = [[0 for _ in range(2)] for _ in range(2)]
        if exp%2 == 0 : # when exponent is even
            x = power_mat(mat,exp//2)
            result = multiple_matrix(x,x)
        else: # when exponent is odd -> mat^exp = mat^(exp-1)*mat
            x = power_mat(mat,exp-1)
            result = multiple_matrix(x,mat)
        
        return result

# print answer
if n<3:
    print(1)
else:
    print(power_mat(base,n)[0][1])
