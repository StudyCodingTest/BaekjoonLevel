# -*-coding:utf-8 -*-
# 적록색약
#

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# DFS 
def dfs(x,y):
    visited[x][y] = True
    current_color = matrix_color[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<n) and (0<=ny<n) and (visited[nx][ny] == False) and (current_color == matrix_color[nx][ny]):
            dfs(nx,ny)

# Input initialize
n = int(input())
matrix_color = [[0]*n for _ in range(n)]
for x in range(n):
    line_color = input().rstrip()
    for y in range(n):
        matrix_color[x][y] = line_color[y]

# variables for DFS
visited = [[False]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
normal_cnt = 0
handicap_cnt = 0

# Normal person count using DFS
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            normal_cnt += 1

# Red-Green handicap person count using DFS

# First, change Green --> Red
for i in range(n):
    for j in range(n):
        if matrix_color[i][j] == 'G':
            matrix_color[i][j] = 'R'

# Second, start DFS (*** We must initialize visited again!***)
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            handicap_cnt += 1

# Answer
print(normal_cnt, handicap_cnt)