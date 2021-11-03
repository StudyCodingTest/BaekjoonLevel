# 종이의 개수
# 6072ms
import sys
N = int(input())
papers = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
ans = [0,0,0]

def count_papers(N,row,col):
    global ans
    first = papers[row][col]
    for i in range(row,row+N):
        for j in range(col,col+N):
            if first != papers[i][j]: break
        else: continue
        break
    else: # 모두 같은 종이일 때
        ans[first+1] += 1
        return
    # 다른 종이가 있을 때
    for i in range(3):
        for j in range(3):
            count_papers(N//3,row + N//3*i,col + N//3*j)
    return

count_papers(N,0,0)
print(*ans,sep='\n')