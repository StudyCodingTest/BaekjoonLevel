# -*- coding: utf-8 -*-
# 쿼드트리
# 72ms
import sys
input = sys.stdin.readline

origin_matrix = [] # 초기 색종이 행렬
n = int(input()) # nxn 행렬
result = [] # 정답 출력 쌓아놓는곳
for _ in range(n):
    origin_matrix.append(input())

def check_color_paper(x,y,n):
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                result.append("(")
                check_color_paper(x,y,n//2) #1사분면
                check_color_paper(x,y+n//2,n//2) #2사분면
                check_color_paper(x+n//2,y,n//2) #3사분면
                check_color_paper(x+n//2,y+n//2,n//2) #4사분면
                result.append(")")
                return
    result.append(int(check))
    return

check_color_paper(0,0,n)
print(*result,sep="")