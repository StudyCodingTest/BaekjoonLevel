import sys
from collections import deque
sys.stdin = open('input', 'r')

# 문제: 한번에 초기화되어야 하는데 1로 바꿔준 다음 그것이 새로운 판에 반영됨
# --> set에 추가하여 익은 토마토로 바꿔줄 토마토들의 좌표를 중복없이 저장 후 한번에 초기화
# --> 하지만, 시간 복잡도 문제로 인해 queue를 활용함, 처음에 한번에 익은 토마토의 좌표를 q에 넣어준 후 popleft()

# <기존의 풀이방식> --> 시간초가
# 일 수를 카운트하기 위해 day 변수를 따로 두고 중복을 피하기 위해 set 변수를 만들어 준후
# 인접한 아직 익지 않은 토마토들의 좌표를 set에 추가해준 후 1로 다 바꿔준다. 다음 day를 1 증가
# 이후 더 이상 set에 원소가 없는 경우 즉, 더이상 인접한 토마토 중에 익을 토마토가 없는 경우
# 아직 익지 않은 토마토가 있는지 검사 --> -1 출력
# 아니면, day 변수 출력

# <수정된 풀이방식> --> bfs
# bfs 문제의 경우 거의 무조건 queue를 쓴다.
# 처음에 익은 토마토의 위치를 우선적으로 queue에 추가해준 후 while문을 이용하여 상하좌우 탐색
# 인접 토마토중 아직 익지 않은 토마토가 있는 경우 queue에 추가해준 후
# 좌표값을 (익은 토마토의 좌표+1)로 해준다. --> 마치 하루가 지난것과 같음
# 이후 queue가 비어있으면, 즉, 더이상 인접 토마토중 익을 토마토가 없으면 검사 후 출력
# But, 2차원 리스트의 (최대값 -1)을 출력해야한다.
# b/c 처음에 익은 토마토의 좌표가 1로 설정되어 있기 때문에 -1을 해줘야 지나간 일 수만큼 출력된다.

m, n = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()

# 이미 익어있는 경우 탐색
already = True # 모두 익은 경우
cannot = False

for elements in pan:
    if 0 in elements: # 하나라도 안 익은 토마토가 있는 경우
        already = False
        break # 즉시 반복문 벗어남
    else:
        continue
if already:
    print(0)
    exit()

for i in range(n):
    for j in range(m):
        if pan[i][j] == 1: # 익은 토마토인 경우 q에 추가
            q.append((i, j))

while q:
        i, j = q.popleft() # 익은 토마토 좌표 popleft()

        for k in range(4):
            ni = i + dy[k] # 행 탐색
            nj = j + dx[k] # 열 탐색

            if 0 <= ni < n and 0 <= nj < m: # 범위 내에서 탐색
                if pan[ni][nj] == -1:
                    continue
                elif pan[ni][nj] == 0: # 인접 토마토가 아직 익지 않은 경우
                    q.append((ni, nj)) # 익은 토마토로 바꿔준 후 q에 추가
                    pan[ni][nj] = pan[i][j] + 1 # 한번 퍼짐 즉, 하루 지남

for element in pan:
    if 0 in element: # 아직 덜 익은 토마토가 있는 경우
        cannot = True
        break

if cannot:
    print(-1)
else:
    # 처음에 익은 토마토의 좌표가 1로 저장되어 있기 때문에
    # 일 수를 카운트하기 위해서 -1을 해준 후 출력해줘야함
    print(max(map(max, pan)) - 1)

