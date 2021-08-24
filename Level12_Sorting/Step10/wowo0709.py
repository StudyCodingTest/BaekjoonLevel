# 좌표 압축
# 6256ms
import sys
input = sys.stdin.readline
N = int(input())
# 좌표, 순서, 압축 결과
coors = list(map(list,zip(list(map(int,input().split())),range(N),[0]*N)))
coors.sort() # 좌표순으로 정렬
different_coor_cnt = 1
for i in range(1,N):
    if coors[i][0] == coors[i-1][0]: 
        coors[i][2] = coors[i-1][2]
    else: 
        coors[i][2] = different_coor_cnt
        different_coor_cnt += 1
# 순서대로 정렬된 압축 결과
print(*[coor[2] for coor in sorted(coors, key=lambda coor: coor[1])],sep=' ')

