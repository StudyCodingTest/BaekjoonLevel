# 스도쿠
# 952ms(PyPy3)
import sys

def solve_sudoku(cnt):
    global sudoku, coo_mat, row, col, sqr
    if cnt == len(coo_mat):
        for row in sudoku: print(*row)
        sys.exit(0) # 한 가지 경우만 탐색

    i,j = coo_mat[cnt]
    for n in range(1,10):
        if row[i][n] == col[j][n] == sqr[i//3*3+j//3][n] == 0:
            sudoku[i][j] = n
            row[i][n] = col[j][n] = sqr[i//3*3+j//3][n] = 1
            solve_sudoku(cnt+1)
            sudoku[i][j] = 0
            row[i][n] = col[j][n] = sqr[i//3*3+j//3][n] = 0
    return

sudoku, coo_mat = [], []
row = [[0 for _ in range(10)] for _ in range(9)]
col = [[0 for _ in range(10)] for _ in range(9)]
sqr = [[0 for _ in range(10)] for _ in range(9)]
for i in range(9): 
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        n = sudoku[i][j]
        if sudoku[i][j] == 0: coo_mat.append((i,j))
        else: 
            row[i][n] = 1
            col[j][n] = 1
            sqr[i//3*3+j//3][n] = 1

solve_sudoku(0)

# 시간초과
'''
import sys

def solve_sudoku(cnt):
    global sudoku, coo_mat
    if cnt == len(coo_mat):
        for row in sudoku: print(*row)
        sys.exit(0)

    row,col = coo_mat[cnt]
    for n in range(1,10):
        if n not in sudoku[row] + \
                    [row[col] for row in sudoku] + \
                    [sudoku[i][j] for i in range(row//3*3,row//3*3+3)
                                    for j in range(col//3*3,col//3*3+3)]:
            sudoku[row][col] = n
            solve_sudoku(cnt+1)
            sudoku[row][col] = 0
    return

sudoku, coo_mat = [], []
for i in range(9): 
    sudoku.append(list(map(int,input().split())))
    # sudoku.append([0 for _ in range(9)])
    for j in range(9):
        if sudoku[-1][j] == 0: coo_mat.append((i,j))

solve_sudoku(0)
'''
