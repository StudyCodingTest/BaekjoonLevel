import sys
from collections import deque
input = sys.stdin.readline

# 명령어 D
def D_command(n):
    D_n = 2*n
    if D_n> 9999:
        return D_n % 10000
    else:
        return D_n

# 명령어 S
def S_command(n):
    if n == 0:
        return 9999
    else:
        return n-1

# 명령어 L
def L_command(n):
    L_n = n%1000 * 10 + n//1000
    return L_n

# 명령어 R
def R_command(n):
    R_n = n%10 * 1000 + n//10
    return R_n

def bfs(start,end):
    q = deque([[start,""]])
    visited = [False]*10000
    while q:
        cur_node, path = q.popleft()
        D_next_node = D_command(cur_node)
        S_next_node = S_command(cur_node)
        L_next_node = L_command(cur_node)
        R_next_node = R_command(cur_node)

        # Search
        if D_next_node == end:
            return path+"D"
        if S_next_node == end:
            return path+"S"
        if L_next_node == end:
            return path+"L"
        if R_next_node == end:
            return path+"R"

        # 다음 Breadth
        if not visited[D_next_node]:
            q.append([D_next_node,path+"D"])
            visited[D_next_node] = True
        if not visited[S_next_node]:
            q.append([S_next_node,path+"S"])
            visited[S_next_node] = True
        if not visited[L_next_node]:
            q.append([L_next_node,path+"L"])
            visited[L_next_node] = True
        if not visited[R_next_node]:
            q.append([R_next_node,path+"R"])
            visited[R_next_node] = True
    

for _ in range(int(input())):
    a,b = map(int,input().split())

    print(bfs(a,b))

    
