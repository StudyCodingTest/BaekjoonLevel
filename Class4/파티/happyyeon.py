import sys
input = sys.stdin.readline

# villages = [
#  마을 : [출발지로부터 마을까지 걸리는 시간, [[다음 마을1, 시간], [다음 마을2, 시간], ...]]
# ]
n,m,x = map(int,input().split())
villages = dict()

for i in range(1,n+1):
    villages[i] = []


for _ in range(m):
    village, next_village, time = map(int,input().split())
    villages[village][1].append([next_village,time])

# 다익스트라 알고리즘
def search(current,end,time=0):
    global min_value
    if villages[current][0] > time:
        villages[current][0] = time
    
    else:
        return 

    if current == end:
        min_value = min(min_value,time)
        return
    
    for i in villages[current][1]:
        search(i[0],end,i[1]+time)
    return min_value
# [1->x->1] 최소 비용, [2->x->2] 최소 비용, ... 를 구함
node_to_x = []

for i in range(1,n+1):
    min_value = 10000
    node_to_x.append(search(i,x))

print(node_to_x)

