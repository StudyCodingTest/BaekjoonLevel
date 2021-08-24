#문제: 나이순 정렬
#시간: 376ms

import sys


ans = [] # 값을 저장할 리스트
count = 0 # 가입 순서를 카운트할 변수
for _ in range(int(input())):
    age, name = sys.stdin.readline().split()
    ans.append((int(age), name, count)) # 나이를 정수형으로 변환한 후 (나이, 이름, 가입순서) 튜플 형식으로 저장
    count += 1 # 가입순서 1증가
ans.sort(key=lambda x:(x[0], x[2])) # 1.나이 2.가입순서 순으로 정렬
for person in ans: # 나이와 이름을 공백을 구분자로 출력
    print(person[0], person[1], sep=' ')
    