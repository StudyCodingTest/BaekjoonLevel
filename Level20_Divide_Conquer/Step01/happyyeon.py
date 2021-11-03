# -*- coding: utf-8 -*-
# ������ �����
# 88ms
import sys
input = sys.stdin.readline

origin_matrix = [] # �ʱ� ������ ���
white_count = 0 # �� �̻� �ɰ��� �� ���� �� �װ��� �ϳ��� �����̷� �����Ͽ� ī��Ʈ ����\
blue_count = 0
n = int(input()) # nxn ���
for _ in range(n):
    origin_matrix.append(list(map(int,input().split())))

def check_color_paper(x,y,n):
    global white_count ,blue_count
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                check_color_paper(x,y,n//2) #1��и�
                check_color_paper(x,y+n//2,n//2) #2��и�
                check_color_paper(x+n//2,y,n//2) #3��и�
                check_color_paper(x+n//2,y+n//2,n//2) #4��и�

                return
    if check == 0:
        white_count += 1
        return
    elif check == 1:
        blue_count += 1
        return

check_color_paper(0,0,n)
print(white_count,blue_count,sep="\n")


