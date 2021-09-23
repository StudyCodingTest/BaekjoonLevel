# 배수와 약수
# 68ms

import sys
input = sys.stdin.readline

while True :
    first, second = map(int,input().split())
    if (first,second) == (0,0) :
        break

    if first > second and first % second == 0 :
        print("multiple")
    elif first < second and second % first == 0 :
        print("factor")
    else :
        print("neither")