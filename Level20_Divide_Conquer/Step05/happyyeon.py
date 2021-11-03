# -*-coding:utf-8 -*-
# ���� ���3
# 1448ms

n,k = map(int,input().split())
P= 1000000007

# ���� ������ �̿��Ͽ� k^n ���ϱ�(�ð� ������ ���Ͽ�)
def k_power_n(k,n):
    if n==1: # base case
        return k%P
    else: 
        temp = k_power_n(k,n//2)
        if n%2 == 1: #n�� Ȧ���� ��
            return temp*temp*k%P
        else: #n�� ¦���� ��
            return temp*temp%P
# DP�� �̿��Ͽ� ���丮�� ���
lst_factorial = [1]*(n+1)

for i in range(2,n+1):
    lst_factorial[i] = (i*lst_factorial[i-1])%P

# a:���� b:�и� , nCk = n!/k!(n-k)!
a = lst_factorial[n]%P
b = (lst_factorial[k]*lst_factorial[n-k])%P

# �丣���� ������ �̿�
print((a%P)*k_power_n(b,P-2)%P)



