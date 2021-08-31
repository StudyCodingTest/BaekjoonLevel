# RGB 거리
# 68ms
import sys
input = sys.stdin.readline
num_house = int(input())
costs_house = [[0]]  # 비용들 인풋
selects_cost = [[0]*3 for _ in range(num_house+1)] # 해당 색으로 집을 칠했을 때 최솟값들 
for _ in range(1,num_house+1) : 
    costs_house.append(list(map(int,input().split())))

for idx in range(1,num_house+1) :
    if idx == 1 : # 집1부터 시작
        selects_cost[idx] = costs_house[idx]
    else : # 집2의 최소 비용 = 집1+집2 , 집3의 최소 비용 = 집1+집2+집3 , ... 
        selects_cost[idx][0] = costs_house[idx][0] + min(selects_cost[idx-1][1], selects_cost[idx-1][2]) # 빨강으로 칠할때 
        selects_cost[idx][1] = costs_house[idx][1] + min(selects_cost[idx-1][0], selects_cost[idx-1][2]) # 초록으로 칠할 때
        selects_cost[idx][2] = costs_house[idx][2] + min(selects_cost[idx-1][0], selects_cost[idx-1][1])# 파랑으로 칠할 때

print(min(selects_cost[num_house][0],selects_cost[num_house][1],selects_cost[num_house][2])) # 최솟값 출력



















# import sys
# input = sys.stdin.readline

# num_house = int(input())
# costs_house = [[0]] # 집 색칠 비용, "집1"부터 시작
# lst = [0]*(num_house+1)
# for _ in range(num_house) : # 집1,집2,집3,... 
#     costs_house.append(list(map(int,input().split())))

# def temp() :
#     min_value = sys.maxsize
#     for idx in range(1,num_house+1) :
#         min_value = min(min_value, min(costs_house[idx])) # 제일 싼 색을 고른다
    

