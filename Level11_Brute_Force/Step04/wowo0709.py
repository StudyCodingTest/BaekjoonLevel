# 체스판 다시 칠하기
# 108ms
b,w = ['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']
goal_board = [b,w,b,w,b,w,b,w]
N, M = map(int, input().split())
board = []
for row in range(N): board.append(list(input()))
# 전체 체스판 검사
ans = N*M
for i in range(N-8+1):
    for j in range(M-8+1):
        # 체스판 조각 검사
        tmp = 0
        for y in range(8):
            for x in range(8):
                if board[i+y][j+x] != goal_board[y][x]: tmp += 1
        ans = min(ans,tmp,64-tmp)

print(ans)