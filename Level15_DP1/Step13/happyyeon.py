# 전깃줄
# 76ms

# 유효 조건 : A,B 전봇대에서 i->N으로 갈 때 i+1은 N+1 이상이어야 한다.
# --> A 전봇대를 번호순으로 정렬하였을 때 B 전봇대의 LIS(가장 긴 증가하는 부분 수열)를 찾으면 그게 곧 유효 조건이 된다.
import sys
input = sys.stdin.readline

n = int(input())
connections = [] 
for _ in range(n) :
    x,y = map(int,input().split())
    connections.append((x,y))
connections.sort(key = lambda x:x[0]) # X 순으로 정렬
dp = [1]*n # DP memoization 초기화 , dp[0] = 1
# LIS
for i in range(n) :
    for j in range(i) :
        if connections[i][1] > connections[j][1] :
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp)) # 총 전깃줄 개수 - 최대로 연결할 수 있는 전깃줄 개수 = 제거해야할 최소 전깃줄 개수
    




