#문제: 좌표 압축
#시간: 2512ms


import sys


n = int(sys.stdin.readline()) # 입렵받는 수의 개수
ans = sys.stdin.readline().split() # 각 요소들을 string형태의 리스트로 만들어줌
for i in range(n): # 각 요소들을 int형으로 변환
    ans[i] = int(ans[i])

ans_ = sorted(list(set(ans))) # 새로운 리스트에 중복제거, 정렬된 리스트를 저장
x = dict()
for i in range(len(ans_)): # key: 숫자, value: 인덱스 번호
    x[ans_[i]] = i
for num in ans:
    print(x[num], end=' ')

## 중복제거, 정렬된 후 인덱스 값은 해당 인덱스에 해당하는 숫자보다 큰 수의 개수와 같음
# 리스트에서 인덱스 번호를 받아와서 출력하는 것 보다
# dictionary에서 값을 출력하는 것이 더 빠르다는 것을 알 수 있었다.
# list.index(i) --> O(N)
# index[i] --> O(1)