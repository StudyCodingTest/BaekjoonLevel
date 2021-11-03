# -*- coding: utf-8 -*-
# 종이의 개수
# 5736ms
import sys
input = sys.stdin.readline

origin_matrix = [] # 초기 색종이 행렬
minus_count = 0 # 더 이상 쪼개질 수 없을 때 그것을 하나의 색종이로 간주하여 카운트 증가\
zero_count = 0
plus_count = 0
n = int(input()) # nxn 행렬
for _ in range(n):
    origin_matrix.append(list(map(int,input().split())))

def check_color_paper(x,y,n):
    global minus_count, zero_count, plus_count
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                check_color_paper(x,y,n//3) #1사분면
                check_color_paper(x,y+n//3,n//3) #2사분면
                check_color_paper(x,y+(2*n)//3,n//3) #3사분면
                check_color_paper(x+n//3,y,n//3) #4사분면
                check_color_paper(x+n//3,y+n//3,n//3) #5사분면
                check_color_paper(x+n//3,y+(2*n)//3,n//3) #6사분면
                check_color_paper(x+(2*n)//3,y,n//3) #7사분면
                check_color_paper(x+(2*n)//3,y+n//3,n//3) #8사분면
                check_color_paper(x+(2*n)//3,y+(2*n)//3,n//3) #9사분면

                return
    if check == -1:
        minus_count += 1
        return
    elif check == 0:
        zero_count += 1
        return
    elif check == 1:
        plus_count += 1
        return

check_color_paper(0,0,n)
print(minus_count,zero_count,plus_count,sep="\n")