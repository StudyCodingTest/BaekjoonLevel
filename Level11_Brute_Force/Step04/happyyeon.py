# 체스판 다시 칠하기
# 182ms

import sys

len_col, len_row = map(int, sys.stdin.readline().split()) # N,M

chess_lines = [] # 8X8 체스판 한 행씩 
modify_count = [] # 색칠 카운트

for i in range(len_col):
    chess_lines.append(sys.stdin.readline())

for square_row in range(len_col-7):  # 사각형에서 8X8 체스판이 나올 수 있는 경우의 수
    for square_col in range(len_row-7):
        black_start = 0
        white_start = 0
        # 8X8 체스판에서 흰색 또는 검은색으로 시작하였을 때, 각각의 색칠해야하는 개수
        for chess_col in range(square_row, square_row + 8):
            for chess_row in range(square_col, square_col + 8):             
                if (chess_row + chess_col)%2 == 0:
                    if chess_lines[chess_col][chess_row] == 'W':  # 검은색 시작 
                        black_start += 1  
                    if chess_lines[chess_col][chess_row] == 'B':  # 흰색 시작
                        white_start += 1
                else :
                    if chess_lines[chess_col][chess_row] == 'B':  # 검은색 시작
                        black_start += 1
                    if chess_lines[chess_col][chess_row] == 'W':  # 흰색 시작
                        white_start += 1
        modify_count.append(min(white_start,black_start))   # 흰색시작과 검은색 시작중 최소값을 저장           
                               
# 사각형에서 나올 수 있는 모든 8X8 체스판을 검사해보았을 때 , 수정사항이 가장 적은 것은 ?
print(min(modify_count))