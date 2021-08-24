#문제: N과 M (2)
#시간: 80ms


import sys


def combination(ans):
    if len(ans) == m: # m개 만큼 뽑으면 출력
        print(*ans) # 공백을 구분자로 출력
    else: # 아직 m개 만큼 뽑지 못한 경우
        for i in range(1, n+1): # 1부터 n까지 반복
            if len(ans) >= 1 and ans[-1] >= i: # 만약 리스트에 요소가 있고 그 수보다 작은 수가 들어온다면 continue
                continue
            else: # 더 큰수가 들어온다면
                ans.append(i) # 추가
                combination(ans) # 함수를 재호출하여 m개가 되는지, 추가할 새로운 숫자들을 차례대로 불러옴
                ans.pop() # 출력된 후 뒤에서부터 하나씩 pop


n, m = map(int, sys.stdin.readline().split())
combination([])
