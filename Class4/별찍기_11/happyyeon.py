import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 초기 조건
n = int(input())
plane = [[" " for _ in range(2*n-1)] for _ in range(n)]

def print_star(x,y,n):
    # Base Case
    if n == 3:
        plane[x][y] = "*"
        plane[x+1][y-1] = "*"
        plane[x+1][y+1] = "*"
        for i in range(-2,3):
            plane[x+2][y+i] = "*"
    # General Case
    else:
        print_star(x,y,n//2)
        print_star(x+n//2,y-n//2,n//2)
        print_star(x+n//2,y+n//2,n//2)

print_star(0,n-1,n)

for i in plane:
    print("".join(i))






