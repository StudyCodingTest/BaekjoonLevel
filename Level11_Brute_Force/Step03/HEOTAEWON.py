#문제: 덩치
#번호: 7568
#시간: 76ms


import sys


dungchi = [] # 각 사람별 몸무게와 키를 저장할 리스트
rank = [] # 등수를 저장할 리스트
for _ in range(int(input())): # 튜플형태로 저장
    n, m = map(int, sys.stdin.readline().split())
    dungchi.append((n, m))

for i in range(len(dungchi)): #본인보다 몸무게와 키 둘 다 큰 사람들을 카운트
    count = 0
    for j in range(len(dungchi)):
        if i == j:
            continue
        if dungchi[j][0]>dungchi[i][0] and dungchi[j][1]> dungchi[i][1]:
            count += 1
    rank.append(count+1) # 본인보다 덩치가 큰 사람들 수 +1이 등수이므로 1을 더해서 저장
for r in rank: # 등수 출력
    print(r, end=' ')
