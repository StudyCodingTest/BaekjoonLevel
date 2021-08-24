#문제: Fly me to the Alpha Centauri
#번호: 1011
#시간: 1324ms

import sys


testcase = int(input()) # 테스트 경우의 수
test = [] # 각 테스트를 저장할 리스트
for _ in range(testcase): # 각 테스트 별 시작과 도착을 저장
    start, arrive = map(int, sys.stdin.readline().split())
    test.append([start, arrive])
for i in range(testcase):
    distance = test[i][1] - test[i][0] # 도착-시작 --> 거리
    count = 0 # 이동횟수 카운트
    move = 1 # 이동거리
    total = 0 # 최종 이동한 거리
    while total < distance: # 목표에 도달할 때까지 반복
        count += 1 # 이동횟수 1증가
        total += move # 이동한만큼 이동거리 추가
        if count % 2 == 0: # 2번마다 이동거리가 1씩 증가하는 규칙
            move += 1
    print(count) # 최종 이동횟수 출력

## 정답을 쭉 나열해보면 2번마다 이동거리가 1씩 증가하는 규칙을 찾을 수 있다.
