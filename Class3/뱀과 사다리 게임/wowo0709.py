from collections import deque
def bfs():
    # visited = [False for _ in range(101)]
    moves = [float('inf') for _ in range(101)]
    moves[0] = 0
    q = deque([(1,0)]) # 위치, 이동횟수
    # visited[0] = True
    while q:
        cur, move = q.popleft()
        if cur >= 100:
            moves[100] = min(move, moves[100])
            continue
        if move > moves[cur]:
            continue
        for i in range(1,7):
            if cur+i in ladders: next = ladders[cur+i]
            elif cur+i in snakes: next = snakes[cur+i]
            else: next = cur+i
            if (next >= 100 and move+1 < moves[100]) or (next < 100 and move+1 < moves[next]):
                q.append((next,move+1))
                moves[next] = move+1
    return moves[100]

N, M = map(int, input().split())
ladders, snakes = dict(), dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v
print(bfs())