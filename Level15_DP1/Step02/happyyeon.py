# 신나는 함수 실행
# 108ms

import sys
input = sys.stdin.readline

memoizations = [[[0]*21 for i in range(21)] for j in range(21)] # 중복 계산 방지

def w(a,b,c) :
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20 : 
        return w(20, 20, 20)
    # w(a,b,c) 존재하는 경우(memoization)
    elif memoizations[a][b][c] :
        return memoizations[a][b][c]
    # w(a,b,c) 존재하지 않는 경우(recursion)
    elif a < b and b < c :
        memoizations[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memoizations[a][b][c]
    else :
        memoizations[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memoizations[a][b][c]
    
while True :
    a,b,c = map(int,input().split())

    if a==-1 and b==-1 and c==-1 :
        break
    print("w({0}, {1}, {2}) = {3}".format(a,b,c,w(a,b,c)))

