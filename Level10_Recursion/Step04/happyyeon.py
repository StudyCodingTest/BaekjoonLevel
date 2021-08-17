# 하노이탑
# 888ms

import sys


# hanoi_tracks = []  # 하노이 이동 경로

# 하노이 이동(원판 수, 출발지, 목적지, 여분 막대)
def move_hanoi(plate,origin,dest,spare) :
    if plate == 1 : # Base Case
        print(origin, dest)
        return
    # General Case
    move_hanoi(plate-1,origin,spare,dest)
    print(origin, dest)
    move_hanoi(plate-1,spare,dest,origin)

plate = int(sys.stdin.readline())
print(2**plate-1)
# 1-출발지 2- 여분 막대 3- 목적지
move_hanoi(plate,1,3,2) 
