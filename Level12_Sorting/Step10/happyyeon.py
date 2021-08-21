# 좌표 압축
# 2292ms

import sys

n = int(sys.stdin.readline())

dots = list(map(int,sys.stdin.readline().split())) # 좌표점들

rank_dots = sorted(list(set(dots))) # 중복 요소 제거 후 정렬 , 인덱스 = 자기보다 낮은 점의 개수

dict_dots = {rank_dots[i] : i for i in range(len(rank_dots))}  # list.index()를 사용하면 시간복잡도 O(n) 
                                                 ## dictionary를 사용하면 시간복잡도 O(1)
for dot in dots : # 결과 출력
    print(dict_dots[dot],end=" ")

