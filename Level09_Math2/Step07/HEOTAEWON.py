#문제: 직사각형에서 탈출
#번호: 1085
#시간: 76ms

import sys


x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, (w-x), (h-y)))

##원점과 꼭지점 중 가장 짧은 곳을 출력
