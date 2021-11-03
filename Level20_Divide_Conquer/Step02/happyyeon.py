# -*- coding: utf-8 -*-
# ����Ʈ��
# 72ms
import sys
input = sys.stdin.readline

origin_matrix = [] # �ʱ� ������ ���
n = int(input()) # nxn ���
result = [] # ���� ��� �׾Ƴ��°�
for _ in range(n):
    origin_matrix.append(input())

def check_color_paper(x,y,n):
    check = origin_matrix[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != origin_matrix[i][j]:
                result.append("(")
                check_color_paper(x,y,n//2) #1��и�
                check_color_paper(x,y+n//2,n//2) #2��и�
                check_color_paper(x+n//2,y,n//2) #3��и�
                check_color_paper(x+n//2,y+n//2,n//2) #4��и�
                result.append(")")
                return
    result.append(int(check))
    return

check_color_paper(0,0,n)
print(*result,sep="")