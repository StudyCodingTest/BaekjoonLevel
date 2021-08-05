# 문제 이름 : 부녀회장이 될 테야!
# 문제 번호 : 2775
# 소요 시간 : 72ms

import sys

t = int(sys.stdin.readline()) # 테스트 케이스 입력 받음

for i in range(t) :
    k = int(sys.stdin.readline()) # K 층
    n = int(sys.stdin.readline()) # N 호
    current_floor_people = [i for i in range(1, n+1)] # Base case : 1,2,3, ... , n = 0층
    next_floor_people = [0 for i in range(n)] # 다음 층 초기화
    for floor in range(k):
        people_sum = 0  # 해당 층 사람 총합
        for i in range(n) :
            people_sum += current_floor_people[i] # 등차수열
            next_floor_people[i] = people_sum 
        current_floor_people = next_floor_people  # General case

    print(current_floor_people[n-1]) # 해당 호실의 사람 수
     

    