import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
paper = [] # 모눈종이
for i in range(n):
    paper.append(list(map(int,input().split())))


def bfs(graph, start_node):
    visit = list()
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit

def check_zero(x,y):
    count = 0

    for i in range(4):
        if paper[x+dx[i]][y+dy[i]] == 0:
            count += 1
            zero_list.append((x+dx[i],y+dy[i]))
    
    return count

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    zero_list = []
    for j in range(m):
        if paper[i][j] == 1 and check_zero(i,j) >=2 :
            for k in range(len(zero_list)):
                bfs(zero_list)
