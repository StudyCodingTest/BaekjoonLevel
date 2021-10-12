#-*- coding: utf-8 -*-
# 프린터 큐
# 80ms

# 중요도 큐의 이동과 인덱스 큐의 이동을 동시에 반영하는 것이 포인트이다.
import sys
input = sys.stdin.readline

for _ in range(int(input())) : # 테스트 케이스
    n,m = map(int,input().split())
    importants = list(map(int,input().split())) # 중요도 큐
    list_index = list(range(len(importants))) # 각 중요도의 인덱스들
    list_index[m] = "target" # m번째 위치한 인덱스 = 타겟

    order = 0 # 출력 순서

    while True :
        if importants[0] == max(importants) : #첫번째 원소가 최댓값이라면 출력순서 1 증가
            order += 1

            if list_index[0] == "target" : #동시에 그 원소가 타겟이라면 해당 순서를 출력
                print(order)
                break
            else : # target이 아니라면
                importants.pop(0) # 그냥 빼내고
                list_index.pop(0) # 인덱스도 그냥 빼낸다
        else : # 첫 번째 원소가 최댓값이 아니라면
            # 원소를 큐 끝에 보내고
            importants.append(importants.pop(0))
            # 그 인덱스도 리스트 끝에 보낸다
            list_index.append(list_index.pop(0))

