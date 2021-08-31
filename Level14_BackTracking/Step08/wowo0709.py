# 스타트와 링크
# 1번 풀이: combinations 모듈 사용, 2964ms(Python3)/624ms(PyPy3)
N = int(input())
S = []
for _ in range(N): S.append(list(map(int, input().split())))
minDiff = float('inf')

from itertools import combinations as C

for teamCase in list(C(range(N),N//2)):
    if teamCase[0] != 0: break # 조합의 총 경우의 수의 반만 검사
    diff = 0
    for (i,j),(k,l) in zip(C(teamCase,2),C(list(set(range(N))-set(teamCase)),2)):
        diff = diff + (S[i][j]+S[j][i]) - (S[k][l]+S[l][k])
    minDiff = min(minDiff,abs(diff))
print(minDiff)



# 2번 풀이: 재귀 백트래킹, 1452ms(Python3)/756ms(PyPy3)
from itertools import combinations as C

def backtracking(cnt, lastPlayer):
    global players, minDiff
    if cnt == N//2:
        diff = 0
        for (i,j),(k,l) in zip(C(players,2),C(list(set(range(N))-set(players)),2)):
            diff = diff + (S[i][j]+S[j][i]) - (S[k][l]+S[l][k])
        minDiff = min(minDiff,abs(diff))
        return

    for player in range(lastPlayer+1,N): # 오름차순(조합)
        players.append(player)
        backtracking(cnt+1,player)
        players.pop()

N = int(input())
S = []
for _ in range(N): S.append(list(map(int, input().split())))
minDiff = float('inf')
players = [0] # 조합의 총 경우의 수의 반만 검사
backtracking(1,0) 
print(minDiff)