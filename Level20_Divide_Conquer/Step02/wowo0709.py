# 쿼드트리
# 84ms
def quadtree(N, cmap):
    if sum(map(sum,cmap)) == 0 or sum(map(sum,cmap)) == N**2:
        return str(cmap[0][0])
    else:
        return '(' +\
                quadtree(N//2, [l[:N//2] for l in cmap[:N//2]]) +\
                quadtree(N//2, [l[N//2:] for l in cmap[:N//2]]) +\
                quadtree(N//2, [l[:N//2] for l in cmap[N//2:]]) +\
                quadtree(N//2, [l[N//2:] for l in cmap[N//2:]]) +\
                ')'


N = int(input())
cmap = [list(map(int,list(input()))) for _ in range(N)]
print(quadtree(N, cmap))