# 문제 이름 : Fly me to the Alpha Centauri
# 문제 번호 : 1011
# 소요 시간 : 84ms

import sys
import math

# def find_triangle_num(order) : # 삼각수 찾기
#     if order == 1:
#         return 1
#     return order + find_triangle_num(order-1)

for i in range(int(sys.stdin.readline())) :
    x, y = map(int, sys.stdin.readline().split())
    distance = y-x # 이동 거리
    root_distance = math.sqrt(distance)
    int_root_distance = int(root_distance)
    move_count = 2 * int_root_distance - 1 # 이동 횟수
    if int_root_distance == root_distance : # 1,2,3, ... root_distance, ..., 3,2,1
        print(move_count) 
    
    # 거리가 제곱수가 아닐 때 이동 횟수가 변하는 기준
    elif distance - int_root_distance ** 2 < ((int_root_distance + 1) ** 2 - int_root_distance ** 2) / 2 :
        print(move_count + 1)  
    else :
        print(move_count + 2)
     

# 거리     이동 횟수
# 1            1
# 2            2
# 3            3
# 4            3
# 5            4
# 6             4
# 7             5
# 8             5
# 9             5
# 10            6
# 11            6
# 12            6
# 13            7
# 14            7
# 15            7
# 16            7
# 17            8
# 18            8
