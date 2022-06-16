import sys
from math import gcd
X = int(1e+9) + 7

def get_converted_integer(a, b): # 기약분수(a/b)를 정수로 변환
    return a * get_square_number(b, X-2) % X

def get_square_number(n, exp): # 제곱수 계산
    if exp == 1:
        return n
    if exp % 2 == 0:
        root_n = get_square_number(n, exp//2)
        return root_n * root_n % X
    else:
        return n * get_square_number(n, exp-1) % X

M = int(sys.stdin.readline())
ans = 0
for _ in range(M):
    # n 면체, 총합 s
    n, s = map(int, sys.stdin.readline().rstrip().split())
    # 기약분수 구하고
    _gcd = gcd(n, s)
    a, b = s // _gcd, n // _gcd
    # 정수로 바꾸고
    num = get_converted_integer(a, b)
    # 답에 더하고
    ans = (ans + num) % X
print(ans)