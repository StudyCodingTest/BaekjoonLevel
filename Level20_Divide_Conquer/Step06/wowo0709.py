# �뻾�젹 ??�깆???
# 256ms
N, M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M, K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

print(*[" ".join(map(str,c)) for c in C],sep='\n')
