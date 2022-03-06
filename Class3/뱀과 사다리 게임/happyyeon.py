# Snake and ladder game
# 

import queue
from shutil import move
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# BFS collect code
def bfs():
    # start
    queue = deque([1]) 
    visited[1] = True

    while queue:
        now = queue.popleft()
        for i in range(1,7): # for add 1~6
            move_position = now + i
            if 1<=move_position<=100 and not visited[move_position]:
                # yes ladder or snake
                if move_position in ladders.keys():
                    move_position = ladders[move_position]
                if move_position in snakes.keys():
                    move_position = snakes[move_position]
                # no ladder or snake
                if not visited[move_position]:
                    queue.append(move_position)
                    visited[move_position] = True
                    board[move_position] = board[now] + 1
                
# Input setting
n,m = map(int,input().split())
board = [0]*101
visited = [False]*101
ladders = dict()
snakes = dict()

# Link dictionary
for i in range(n+m):
    x,y = map(int,input().split())
    if x < y:
        ladders[x] = y
    else:
        snakes[x] = y

bfs()
print(board[100])

# count = 0
# BFS error code
# def bfs(n):
#     global count
#     if n == 1:
#         return
#     candidates = [] 
#     for i in range(1,7):
#         next_node = n-i
#         if graph[next_node] and graph[next_node] < next_node:
#             candidates.append(graph[next_node])
#     if candidates: # ladder >= 2 --> jump maximum
#         count += 1
#         bfs(min(candidates))
#     else:
#         count += 1
#         bfs(graph[n-6]) # No ladder --> move min num