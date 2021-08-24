#문제: N과 M (4)
#시간: 104ms


import sys


def choose(ans):
    if len(ans) == m: # m개를 뽑으면 출력
        print(*ans)
    else:
        for i in range(1, n+1): # 1부터 n까지 반복
            if len(ans) >= 1 and ans[-1] > i: # 오름차순으로 추가
                continue
            ans.append(i) # m개를 뽑을 때까지 하나씩 추가
            choose(ans) # m개 되었는지 검사, 새로 1부터 n까지 뽑음
            ans.pop() # 출력된 후 뒤에서부터 pop


n, m = map(int, sys.stdin.readline().split())
choose([])
