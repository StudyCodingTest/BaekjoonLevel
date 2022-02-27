N, M = map(int, input().split())
dist = [[float('inf') for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    dist[a-1][b-1], dist[b-1][a-1] = 1, 1
for i in range(N):
    dist[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans = [float('inf'),0] # 케빈 베이컨 수, 사람 번호
for i in range(N):
    kb_num = sum([dist[i][j] for j in range(N)])
    if ans[0] > kb_num:
        ans = [kb_num, i+1]
print(ans[1])