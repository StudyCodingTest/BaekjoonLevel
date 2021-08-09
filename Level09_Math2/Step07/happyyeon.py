# 문제 이름 : 직사각형에서의 탈출
# 문제 번호 : 1085
# 소요 시간 : 84ms

import sys

x,y,w,h = map(int,sys.stdin.readline().split())

distances = [x,y,w-x,h-y]

print(min(distances))

