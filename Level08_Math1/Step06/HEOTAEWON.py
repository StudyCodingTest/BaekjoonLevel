#문제: 부녀회장이 될테야
#번호: 2775
#시간: 76ms
import sys


testcase = int(input()) #테스트 횟수 변수를 따로 선언하여 받는다.
building = [] #각 테스트별로 층, 호 수를 저장할 리스트를 선언한다.

for _ in range(testcase): #테스트횟수만큼 반복한다.
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    building.append([n, k]) #이중리스트로 만들어준다.
for x in range(testcase): #테스트 횟수만큼 반복한다.
    house = [] #테스트를 시작할 때마다 호 수별 사람의 수를 저장할 리스트 초기화
    for i in range(1, building[x][1]+1): #0층의 사람수를 range()를 이용하여 추가한다.
        house.append(i)
    for _ in range(building[x][0]): #층수만큼 반복한다.
        for m in range(1, building[x][1]): #모든층의 1호는 1명이므로 1번 인덱스부터 수정한다.
            house[m] += house[m-1] #이전 호수들의 합으로 계속 수정해간다.
    print(house[-1]) #주어진 입력의 마지막 층, 마지막 호수의 사람수를 출력한다.

##testcase변수를 따로 선언하지 않고 range(int(input())을 사용하려 하였으나,
##입력이 끝난후 이어서 바로 출력이 되는 오류로 인해 정상적인 정답이 출력되지 않았다.
