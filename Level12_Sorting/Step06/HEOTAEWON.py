#문제: 좌표 정렬하기
#시간: 444ms


import sys


point = [] # 입력받은 좌표를 저장할 리스트
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y)) # 좌표를 튜플 형식으로 저장
point.sort(key=lambda x: (x[0], x[1])) # key를 x로 첫번째 순으로 정렬, 만약 첫번째가 같다면 두번째 순으로 오름차순 정렬
for i in range(len(point)): # 공백을 구분자로 하여 x, y를 출력
    print(point[i][0], point[i][1], sep=' ')
