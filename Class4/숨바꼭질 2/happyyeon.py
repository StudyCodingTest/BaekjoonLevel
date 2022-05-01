import sys
from collections import deque,defaultdict
input = sys.stdin.readline

subin,brother = map(int,input().split())

def bfs(start):
    visited = [0]*100001
    queue = deque([(start,0)])
    count_way_time = defaultdict(int) # 동생을 찾는 가장 빠른 시간의 경로 개수

    while queue:
        cur_node, count = queue.popleft()
        visited[cur_node] = 1
        # 현재 노드가 동생 노드인 경우
        if cur_node == brother:
            count_way_time[count] += 1
        # 앞으로 걷는 경우 = 현재 노드 + 1
        if 0<=cur_node+1<=100000 and visited[cur_node+1]==0:
            queue.append((cur_node+1,count+1))
        # 뒤로 걷는 경우 = 현재 노드 - 1
        if 0<=cur_node-1<=100000 and visited[cur_node-1]==0:
            queue.append((cur_node-1,count+1))
        # 순간이동 하는 경우 = 현재 노드 * 2
        if 0<=cur_node*2<=100000 and visited[cur_node*2]==0:
            queue.append((cur_node*2,count+1))

    return count_way_time

fast_time = int(1e9)
count_way_time = bfs(subin)
# 동생을 찾는 방법의 시간들 = time
# 가장 빠른 시간을 찾음
for time in count_way_time.keys():
    fast_time = min(fast_time,time)

print(fast_time)
print(count_way_time[fast_time])

            
            
        
        
        
