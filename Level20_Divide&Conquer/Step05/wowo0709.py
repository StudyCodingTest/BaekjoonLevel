# 이항 계수 3
# 
'''
[페르마의 소정리]
- a^(p-1) <=> 1 (mod p) // p는 소수이고 a는 p의 약수가 아닌 정수
- a^k % p = a'^p % p = a' % p
- 예: 4^15를 5로 나눈 나머지는 몇인가?
  4^15 = (4^3)^5 = 64^5 = 64%5 = 4
- 이항 계수: nCr = n!/(r!(n-r)!) % p (A = n!, B = (r!(n-r)!)
            -> (A * B^(-1)) % p
            -> ((A % p) * (B^(-1) % p)) % p
            -> ((A % p) * B^(p-2)) % p
- 결과적인 시간복잡도는 O(N + logN)
'''
def cal_power(n,k,c): # n^k
    if k in memo: pow = memo[k]
    elif k % 2 == 0: pow = cal_power(n,k//2,c) * cal_power(n,k//2,c)
    else: pow = cal_power(n,1,c) * cal_power(n,k-1,c)
    
    if k not in memo: memo[k] = pow % c
    return memo[k] % c

n, k = map(int,input().split())
numerator,denominator,div = 1,1,int(1e+9 + 7)
# STEP 1. 페르마의 정리에 따라 얻은 이항계수 변환식의 n!, k!, (n-k)! 구하기
for i in range(2,n+1):
    numerator *= i
    numerator %= div
for j in range(2,k+1):
    denominator *= j
    denominator %= div
for k in range(2,n-k+1):
    denominator *= k
    denominator %= div
# STEP 2. 분모의 (p-2) 제곱 구하기
memo = {0:1,1:denominator}
denominator = cal_power(denominator,div-2, div)
# STEP 3. 최종적으로 답 구하기
print(numerator*denominator%div)