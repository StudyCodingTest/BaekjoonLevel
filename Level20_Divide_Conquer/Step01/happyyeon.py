# -*- coding: utf-8 -*-
# 색종이 만들기
# 88ms
import sys
input = sys.stdin.readline

origin_matrix = [] # 초기 색종이 행렬
white_count = 0 # 더 이상 쪼개질 수 없을 때 그것을 하나의 색종이로 간주하여 카운트 증가\
blue_count = 0
n = int(input()) # nxn 행렬
for _ in range(n):
    origin_matrix.append(list(map(int,input().split())))

def check_color_paper(x,y,n):
    global white_count ,blue_count
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                check_color_paper(x,y,n//2) #1사분면
                check_color_paper(x,y+n//2,n//2) #2사분면
                check_color_paper(x+n//2,y,n//2) #3사분면
                check_color_paper(x+n//2,y+n//2,n//2) #4사분면

                return
    if check == 0:
        white_count += 1
        return
    elif check == 1:
        blue_count += 1
        return

check_color_paper(0,0,n)
print(white_count,blue_count,sep="\n")


