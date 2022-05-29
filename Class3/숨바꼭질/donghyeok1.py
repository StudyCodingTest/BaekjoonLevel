import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False] * 100001

def bfs(N, K, visited):
    queue = deque()
    queue.append([N, 0])
    visited[N] = True
    if N == K:
        print(0)
        return
    
    while queue:
        path, second = queue.popleft()
        
        if K == path:
            print(second)
            break
        else:
            for edit_path in ((path + 1), (path - 1), (path * 2)):
                if 0 <= edit_path <= 100000 and visited[edit_path] == False:
                    queue.append([edit_path, second + 1])
                    visited[edit_path] = True
        
        
            
        
        
        

bfs(N, K, visited) 
        
        
    
    
