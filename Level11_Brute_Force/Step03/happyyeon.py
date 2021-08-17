# 덩치
#80ms
import sys

bulks = [] # 덩치 리스트
for i in range(int(sys.stdin.readline())) :
    bulks.append(tuple(map(int,sys.stdin.readline().split())))

for i in range(len(bulks)) :
    rank = 1 # 덩치 등수
    for j in range(len(bulks)) :
        if bulks[i][0] < bulks[j][0] and bulks[i][1] < bulks[j][1] : # (몸무게, 키)가 둘 다 클 경우
            rank += 1

    print(rank,end=" ")

