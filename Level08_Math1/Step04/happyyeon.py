# 문제 이름 : 달팽이는 올라가고 싶다.
# 문제 번호 : 2869
# 소요 시간 : 72ms

import sys
import math

a,b,v = map(int, sys.stdin.readline().split()) # A,B,V 정수형으로 입력

snail_location = 0 # 달팽이 초기 위치

print(math.ceil((v-a) / (a-b)) + 1) # V-A 위치를 넘기는데까지 걸리는 최소 일 수 + 마지막 0~A(잔챙이 거리)를 올라가는 일 수 = 1일





