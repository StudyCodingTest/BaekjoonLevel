# -*-coding:utf-8 -*-
# ����
# 68ms

import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def k_power_n(k,n):
    if n==1: # base case
        return k%c
    else: 
        temp = k_power_n(k,n//2)
        if n%2 == 1: #n�� Ȧ���� ��
            return temp*temp*k%c
        else: #n�� ¦���� ��
            return temp*temp%c

print(k_power_n(a,b))

