# 문제 이름 : 벌집
# 문제 번호 : 2292
# 소요 시간 : 76ms

import sys

n = int(sys.stdin.readline()) # N 입력 받음
if n == 1 :
    print(1)
else :
    layer = 0 # 벌집 중앙에서부터 각 껍질
    while n - 1 > 0:
        layer += 1
        n -= 6 * layer
    print(layer + 1) # 1번 방은 반드시 거쳐야 하므로 +1을 해주어야 한다.