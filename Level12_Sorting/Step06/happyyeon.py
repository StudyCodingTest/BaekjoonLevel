# 좌표 정렬하기
# 492ms

import sys

dots = [] # 점 리스트

num_dot = int(sys.stdin.readline())

for i in range(num_dot) : # 점들 리스트에 추가
    x,y = tuple(map(int,sys.stdin.readline().split())) 
    dots.append((x,y))

dots.sort()
# 버블 정렬
for idx in range(num_dot-1) :
    if dots[idx][0] == dots[idx+1][0] and dots[idx][1] > dots[idx+1][1] :
        temp = dots[idx]
        dots[idx] = dots[idx+1]
        dots[idx+1] = temp
    else :
        continue

# 결과 출력
for dot in dots :
    print(dot[0], dot[1])



