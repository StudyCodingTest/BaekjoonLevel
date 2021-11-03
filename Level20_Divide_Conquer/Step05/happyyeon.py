# -*-coding:utf-8 -*-
# 이항 계수3
# 1448ms

n,k = map(int,input().split())
P= 1000000007

# 분할 정복을 이용하여 k^n 구하기(시간 단축을 위하여)
def k_power_n(k,n):
    if n==1: # base case
        return k%P
    else: 
        temp = k_power_n(k,n//2)
        if n%2 == 1: #n이 홀수일 때
            return temp*temp*k%P
        else: #n이 짝수일 때
            return temp*temp%P
# DP를 이용하여 팩토리얼 계산
lst_factorial = [1]*(n+1)

for i in range(2,n+1):
    lst_factorial[i] = (i*lst_factorial[i-1])%P

# a:분자 b:분모 , nCk = n!/k!(n-k)!
a = lst_factorial[n]%P
b = (lst_factorial[k]*lst_factorial[n-k])%P

# 페르마의 소정리 이용
print((a%P)*k_power_n(b,P-2)%P)



