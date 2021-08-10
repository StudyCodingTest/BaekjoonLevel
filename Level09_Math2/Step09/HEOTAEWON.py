#문제: 직각삼각형
#번호: 4153
#시간: 72ms

import sys


while True:
    triangle = list(map(int, sys.stdin.readline().split())) #각 변의 길이를 리스트로 저장
    if(triangle[0] == 0): #입력이 0이 들어오면 종료
        break
    triangle.sort() #오름차순으로 정렬
    long = triangle.pop() #가장 큰 길이를 long 변수에 저장 후 리스트에서 삭제

    if long**2 == triangle[0]**2 + triangle[1]**2: #피타고라스 정리를 만족하면
        print('right') #정답 출력
    else: #만족하지 않으면
        print('wrong') #땡 출력
