# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
n,r,c = map(int,input().split())
count = 0 # ī��Ʈ �ʱ�ȭ
while n>=1:
    if r<2**(n-1) and c>=2**(n-1): #2��и�
        count += 4**(n-1)
        c -= (2**(n-1))
    if r>=2**(n-1) and c<2**(n-1): #3��и�
        count += 2*(4**(n-1))
        r -= (2**(n-1))
    if r>=2**(n-1) and c>=2**(n-1): #4��и�
        count += 3*(4**(n-1))
        r -= (2**(n-1))
        c -= (2**(n-1))

    n -= 1
    # n,c,r update
    
print(count)