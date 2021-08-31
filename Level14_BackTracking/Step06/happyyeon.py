# 스도쿠
# 3172ms

import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for i in range (9)] # 스도쿠 판 생성
zeros = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0] # 빈 칸 좌표
# 좌표가 주어졌을 때, 가능한 정답 후보 리턴
def get_possibles(row,col) :
    ######## 가로 체크 ########
    possibles = set(range(1,10)) # 정답 후보 1~9
    test = set(board[row])
    possibles -= test # 겹치는 숫자 제거 --> 정답 후보
    ###### 세로 체크 ########
    test = set() # 테스트셋 초기화
    for i in range(9) : # 세로 체크
        test.add(board[i][col])
    possibles -= test
    ##### 사각형 체크 ######
    test = set()
    for i in range(row//3*3, row//3*3+3) :
        for j in range(col//3*3,col//3*3+3) :
            test.add(board[i][j])
    possibles -= test

    return list(possibles)

def play_sudoku(start) :
    # 빈 칸 다 찾았을 때 출력
    if start == len(zeros) :
        [print(*row) for row in board]
        sys.exit()
    row, col = zeros[start]
    possibles = get_possibles(row,col)

    for num in possibles :
        board[row][col] = num
        play_sudoku(start+1)
        board[row][col] = 0 # 중간에 재귀함수의 해가 없는 경우를 고려

play_sudoku(0)

