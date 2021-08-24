#문제: N과 M (1)
#시간: 260ms


import sys


def permute(ans):
    if len(ans) == m: # 만약 ans길이가 m개와 같아진다면 출력
        print(*ans) # m개만큼만 뽑아야 하기 때문, 공백을 구분자로 출력
    else: # 아직 m개를 뽑지 못했다면
        for i in range(1, n+1): # 1부터 n까지 반복
            if i in ans: # 이미 ans에 있다면 continue --> 중복제거
                continue
            ans.append(i) # ans에 i추가 (순서대로)
            permute(ans) # 다시 함수를 실행하여 m개를 뽑았는지, 다시 숫자를 처음부터 들어있는지 확인
            ans.pop() # m개를 뽑은 후 다시 끝자리부터 정렬해야하므로 하나씩 pop

n, m = map(int, sys.stdin.readline().split())
permute([]) # 빈 리스트로 실행

## 만약 i가 ans에 있으면 아래를 수행하지 않고 다시 for문 --> 중복을 없앤다.
# i를 추가
# 함수실행 --> 중복확인 --> 추가 --> 함수실행 --> 출력 --> pop() --> 중복확인

