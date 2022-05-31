import sys
sys.stdin = open('input', 'r')

sys.setrecursionlimit(10 ** 6)


t = int(input())

def dfs(x, y, pan): # (x, y)가 배추인 경우에만 함수를 실행한다.
    # if (x, y) in visited: # 이미 그 영역에서 체크한 경우
    #     return
    # visited.append((x, y))
    for d in range(4): # 상하좌우 탐색
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if pan[nx][ny] == 1: #and (nx, ny) not in visited: # 탐색결과 인접 배추인 경우
                pan[nx][ny] = 0
                dfs(nx, ny, pan) # 재귀를 이용하여 추가 탐색


for _ in range(t):
    m, n, k = map(int, input().split())
    pan = list([0] * m for _ in range(n))

    # visited = []

    for _ in range(k):
        xm, yn = map(int, input().split())
        pan[yn][xm] = 1

    area = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]


    for i in range(n):
        for j in range(m):
            if pan[i][j] == 1: #and (i, j) not in visited:
                dfs(i, j, pan)
                area += 1
    #print(visited)

    print(area)


# check = set()
# for i in range(n):
#     for j in range(m):
#         if pan[i][j] == 1 and (i, j) not in check:
#             check.add((i, j))
#             for d in range(4):
#                 ni, nj = i + dx[d], j + dy[d]
#                 if 0 <= ni < n and 0 <= nj < m: # 범위를 벗어나지 않도록 함
#                     if pan[ni][nj] == 1: # 인접 배추가 있는 경우
#                         area += 1
#                         check.add((ni, nj))
#         else:
#             continue

# print(area)

