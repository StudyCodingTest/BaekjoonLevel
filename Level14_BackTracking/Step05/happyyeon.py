# N-QUEEN 
# 

import sys

n = int(sys.stdin.readline()) 

count = 0  # 퀸 착수 경우의 수
col = [0] * (n+1) # NxN 체스판 -> col = [0,1,2,...,N] --> N+1개


def check_promising(x,col) :
    row = 1 # 1행부터 시작 (테스트 행)
    flag = True # 퀸의 충돌 시, False로 바꿀 예정
    while flag and row < x : # 유망하지 않거나 테스트 행이 x 값과 같아지면 탈출
        if (col[x] == col[row] or x-row == abs(col[x] - col[row])) : # 열의 충돌 or 대각 충돌
            flag = False
        row += 1 # 충돌 없으면 다음 행 검사 

    return flag

# N-QUEEN 출력 함수(NxN 체스판을 (1,1),(1,2) ... (x,y) 좌표로 바라보았을 때.)
# col[x] -> x행에 놓여진 퀸의 y값 --> (x,y)의 y
def n_queen(x, col) :
    global count
    max_depth = len(col) - 1 # 행의 최대 개수
    
    if(check_promising(x,col)) : # 퀸 착수 위치가 유망하다면
        if x == max_depth : # 최대 깊이까지 탐색하여 퀸을 전부 착수 하였다면
            count += 1 # 퀸 착수 경우의 수 추가

        else : # 최대 깊이까지 전부 탐색하지 않았다면
            for y in range(1,max_depth+1) : # 1부터 끝까지 열의 위치
                col[x+1] = y # (x+1,1), (x+1,2), (x+1,3) ... 착수해 봄
                n_queen(x+1,col) # x+1 행의 유망도 검사 , 유망하지 않다면 아무것도 반환되지 않음.

n_queen(0,col) 
print(count) 
