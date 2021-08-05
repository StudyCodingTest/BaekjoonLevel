# 문제 이름 : ACM 호텔
# 문제 번호 : 10250
# 소요 시간 : 72ms

import sys
import math

t = int(sys.stdin.readline()) # 테스트 개수

for i in range(t) : 
    h,w,n = map(int,sys.stdin.readline().split()) # H,W,N
    
    room_number = math.ceil(n/h)  # XXYY 호에서 YY에 해당
    if n % h == 0 : # XXYY 호에서 XX에 해당
        floor_number = h
    else :
        floor_number = n % h  

    if room_number < 10 : # 101호 , 201호 이런 식으로 중간에 0이 껴있어야함.
        print("{0}0{1}".format(floor_number, room_number))
    else :
        print("{0}{1}".format(floor_number, room_number)) 
