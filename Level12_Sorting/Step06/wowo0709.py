# 좌표 정렬하기
# 384ms
import sys
input = sys.stdin.readline

coors = []
for _ in range(int(input())): coors.append(tuple(map(int,input().split())))
coors.sort(key=lambda coor: (coor[0], coor[1]))
for coor in coors: print(*coor)