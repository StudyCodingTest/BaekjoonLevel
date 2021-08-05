# 문제 이름 : 상수
# 문제 번호 : 2908
# 소요 시간 : 80ms

import sys

a, b = map(str, sys.stdin.readline().split()) # 칠판에 적은 두 수 A B

print(max(int(a[::-1]), int(b[::-1]))) # 상수의 대답