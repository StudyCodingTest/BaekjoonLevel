# 별 찍기 - 10
# 1260ms

# x, y는 좌상 시작점
def make_star_board(n, x, y):
    global board
    if n == 1:
        board[y][x] = '*'
        return
    for nx in [0, n//3, 2*n//3]:
        for ny in [0, n//3, 2*n//3]:
            if nx == ny == n//3: continue
            make_star_board(n//3, x+nx, y+ny)

N = int(input())
board = [[' ' for _ in range(N)] for _ in range(N)]
make_star_board(N, 0, 0)
for stars in board: print(''.join(stars))