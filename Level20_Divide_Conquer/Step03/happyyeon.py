# -*- coding: utf-8 -*-
# ������ ����
# 5736ms
import sys
input = sys.stdin.readline

origin_matrix = [] # �ʱ� ������ ���
minus_count = 0 # �� �̻� �ɰ��� �� ���� �� �װ��� �ϳ��� �����̷� �����Ͽ� ī��Ʈ ����\
zero_count = 0
plus_count = 0
n = int(input()) # nxn ���
for _ in range(n):
    origin_matrix.append(list(map(int,input().split())))

def check_color_paper(x,y,n):
    global minus_count, zero_count, plus_count
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                check_color_paper(x,y,n//3) #1��и�
                check_color_paper(x,y+n//3,n//3) #2��и�
                check_color_paper(x,y+(2*n)//3,n//3) #3��и�
                check_color_paper(x+n//3,y,n//3) #4��и�
                check_color_paper(x+n//3,y+n//3,n//3) #5��и�
                check_color_paper(x+n//3,y+(2*n)//3,n//3) #6��и�
                check_color_paper(x+(2*n)//3,y,n//3) #7��и�
                check_color_paper(x+(2*n)//3,y+n//3,n//3) #8��и�
                check_color_paper(x+(2*n)//3,y+(2*n)//3,n//3) #9��и�

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