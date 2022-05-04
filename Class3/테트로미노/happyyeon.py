import sys
input = sys.stdin.readline

# 초기값 세팅
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
answer = 0 # 최종 정답
# 테트로미노 모든 경우의수
tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

def find(x,y):
    global answer
    for i in range(19):
        result = 0 # 블록 하나 놓아봤을 때 결과값
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0]
                next_y = y + tetromino[i][j][1]
                result += matrix[next_x][next_y]
            except:
                break
        answer = max(answer,result)

# 완전탐색
for i in range(n):
    for j in range(m):
        find(i,j)

print(answer)
    