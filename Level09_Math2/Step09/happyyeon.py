# 문제 이름 : 직각삼각형
# 문제 번호 : 4153
# 소요 시간 : 72ms

import sys

while True :
    # 삼각형 3개의 변 
    triangle_line1, triangle_line2, triangle_line3 = map(int,sys.stdin.readline().split())

    # 종료 조건
    if (triangle_line1, triangle_line2, triangle_line3) == (0,0,0) :
        break
    
    triangle_lines = [triangle_line1, triangle_line2, triangle_line3]
    # 길이 순으로 정렬
    triangle_lines.sort()
    # 피타고라스 정리 
    if triangle_lines[0] ** 2 + triangle_lines[1] **2 == triangle_lines[2] ** 2 : 
        print("right")
    else :
        print("wrong")
       