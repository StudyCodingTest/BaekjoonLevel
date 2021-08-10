#문제: 네 번째 점
#번호: 3009
#시간: 76ms

import sys


point = [] # 각 점들의 좌표를 저장할 리스트
point_x = [] # 각 점들의 x좌표만 저장할 리스트
point_y = [] # 각 점들의 y좌표만 저장할 리스트
#좌표들을 리스트로 저장
point1 = list(map(int, sys.stdin.readline().split()))
point2 = list(map(int, sys.stdin.readline().split()))
point3 = list(map(int, sys.stdin.readline().split()))
#2중리스트 형태로 추가ㅣ
point.append(point1)
point.append(point2)
point.append(point3)
#x좌표, y좌표끼리 저장
for i in range(3):
    point_x.append(point[i][0])
    point_y.append(point[i][1])
#좌표의 개수가 1개인 점들을 출력
for i in range(3):
    if point_x.count(point_x[i]) == 1:
        print(point_x[i], end=' ')
for i in range(3):
    if point_y.count(point_y[i]) == 1:
        print(point_y[i])

## 직사각형이 되려면 중복되는 x, y좌표가 2개씩 있어야한다는 것에 아이디어를 얻음
# for문 한번에 x, y둘 다 출력하려 했으나 어느 것이 먼저 출력되는지에 따라
# 공백이 들어가서 틀리는 오류가 있었다. 그래서 x먼저 출력한 후 y를 출력하였다.