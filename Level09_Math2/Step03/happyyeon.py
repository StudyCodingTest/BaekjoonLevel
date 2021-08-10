# 문제 이름 : 소인수분해
# 문제 번호 : 11653
# 소요 시간 : 1584ms

import sys

n = int(sys.stdin.readline())
# 변수 초기화
devider = 2

# 소인수분해
while n != 1 :
    if n % devider == 0 :
        print(devider)
        n = n//devider
    else :
        devider += 1





