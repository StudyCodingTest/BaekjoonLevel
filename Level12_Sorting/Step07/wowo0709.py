# 좌표 정렬하기 2
# 444ms
import sys
input = sys.stdin.readline

coors = []
for _ in range(int(input())): coors.append(tuple(map(int,input().split())))
coors.sort(key=lambda coor: (coor[1], coor[0]))
for coor in coors: print(*coor)