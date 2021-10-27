# 색종이 만들기
# 112ms
def make_paper(N, papers, cnt):
    if sum(map(sum,papers)) == 0 or sum(map(sum,papers)) == N**2:
        return [cnt[0]+1,cnt[1]] if papers[0][0] == 0 else [cnt[0],cnt[1]+1]
    else:
        cnt = [p1+p2+p3+p4 for p1,p2,p3,p4 in zip(
                make_paper(N//2, [l[:N//2] for l in papers[:N//2]],cnt),
                make_paper(N//2, [l[N//2:] for l in papers[:N//2]],cnt),
                make_paper(N//2, [l[:N//2] for l in papers[N//2:]],cnt),
                make_paper(N//2, [l[N//2:] for l in papers[N//2:]],cnt)
        )]
        return cnt


N = int(input())
papers = [list(map(int,input().split())) for _ in range(N)]
print(*make_paper(N, papers, [0,0]), sep='\n')
