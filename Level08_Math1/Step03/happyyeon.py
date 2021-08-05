# 문제 이름 : 분수 찾기
# 문제 번호 : 1193
# 소요 시간 : 76ms

import sys

x = int(sys.stdin.readline()) # X 
save_x = x # 아래 while문에서 x를 건드릴 것이므로 저장 해놓음

if x == 1 :  # X = 1 인 경우는 규칙성에 위배되므로 예외 처리
    print("1/1")
else :
    layer = 0  # 대각선 방향으로 층을 나눈다.
    while x > 0 :
        layer += 1 
        x -= layer 
    start_x_number = 0 # 해당 층에서 X가 몇 번째 위치에 있는지 알기 위해 그 층의 시작 X 숫자를 구한다.
    for count in range(1,layer) : # 1~ layer -1 까지 있는 총 숫자의 개수 
        start_x_number += count
    start_x_number += 1 # 해당 층의 제일 첫번째 혹은 마지막에 있는 숫자
    fractionIndex = save_x - start_x_number # 해당 층에 몇 번째 위치(인덱스)에 있는지 알 수 있음
    # 예를 들어, x = 14 인데 해당 층의 시작 x 넘버 = 11이면 해당 분수는 그 층의 14 -11 = 3번째 인덱스 위치에 존재
     
    if layer % 2 == 1 : # 홀수 층
        print("{0}/{1}".format((layer - fractionIndex), (1 + fractionIndex))) 
    else : # 짝수 층
        print("{0}/{1}".format((1 + fractionIndex), (layer - fractionIndex))) 