# 문제 이름 : 터렛
# 문제 번호 : 1002
# 소요 시간 : 76ms

import sys, math

for test_case in range(int(sys.stdin.readline())):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    # (x1,y1) , (x2,y2) 를 중심축으로 하는 원을 생각해본다.
    distance_between_circles = math.sqrt((x2-x1)**2 + (y2-y1)**2)
     # 원이 완전히 일치 --> 교점 무한 --> 경우의 수 무한
    if distance_between_circles == 0 and r1 == r2 :
        print(-1)
    # 교점이 한 개인 경우 (외접, 내접) --> x3,y3가 생길 수 있는 경우의 수 1
    elif distance_between_circles == r1+r2 or distance_between_circles == abs(r1-r2):
        print(1)
    # 교점이 없는 경우(바깥, 안쪽) --> x3,y3가 생길 수 있는 경우의수 0
    elif distance_between_circles > r1+r2 or distance_between_circles < abs(r1-r2) :
        print(0)
    else :
        print(2)
    
