#문제: 소수 구하기
#번호: 1929
#시간: 6484ms

import sys


M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1): #M부터 N까지 검사
    if i == 1: # 1은 예외
        continue
    for x in range(2, int(i**0.5)+1): #2부터 i의 제곱근까지만 확인(** : 제곱연산), 정수형으로 변환해줘야함
        if i%x == 0:
            break
    else: #for-else문 사용
        print(i)

## 특정 숫자가 그보다 작은 수로 나눠지는가 판별할 때,
# 그 수의 제곱근까지만 확인을 하면 그 이후로는 확인해볼 필요가 없다.
# 왜냐하면 특정 수의 약수를 나열했을 때 반으로 접어서 대칭되는 수를 곱하면 되는 것을 알 수 있다.
# 예를 들면 36 --> 1, 2, 3, 6, 12, 18, 36 과 같다. 즉, 36이 소수인지 판별할 때는 36의 제곱근 6이후로는 확인해볼 필요가 없다.
# 소수의 경우 예를 들면 7 --> 1, 7이다. 역시 대칭이다. 이 경우 7의 제곱근 이후로는 확인해볼 필요가 없다.
# '에라토스테네스의 체' 참고
