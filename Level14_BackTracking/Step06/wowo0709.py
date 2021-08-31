# 스도쿠
# 872ms(PyPy3)
def solve_sudoku(cnt):
    global sudoku, coo_mat, row, col, sqr
    if cnt == len(coo_mat):
        for row in sudoku: print(*row)
        exit(0) # 한 가지 경우만 탐색

    i,j = coo_mat[cnt]
    for n in range(1,10):
        if row[i][n] == col[j][n] == sqr[i//3*3+j//3][n] == 0:
            row[i][n] = col[j][n] = sqr[i//3*3+j//3][n] = 1
            sudoku[i][j] = n
            solve_sudoku(cnt+1)
            sudoku[i][j] = 0
            row[i][n] = col[j][n] = sqr[i//3*3+j//3][n] = 0

sudoku, coo_mat = [], []
row = [[0 for _ in range(10)] for _ in range(9)]
col = [[0 for _ in range(10)] for _ in range(9)]
sqr = [[0 for _ in range(10)] for _ in range(9)]
for i in range(9): 
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        n = sudoku[i][j]
        if n == 0: coo_mat.append((i,j))
        else: row[i][n] = col[j][n] = sqr[i//3*3+j//3][n] = 1

solve_sudoku(0)
