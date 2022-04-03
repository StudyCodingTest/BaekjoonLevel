# 백준 - 1043 , 1트
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

gods = deque(list(map(int,input().split())))
num_god = gods[0] # 신은 모든 걸 알고 있으므로 진실을 아는 사람은 신이다.
gods.popleft() #1. 진실을 아는 자들의 배열을 만든다.
gods = set(gods)
answer = []

def solution():
    for i in range(m):
        party_people = deque(list(map(int,input().split())))
        party_people.popleft()

        #3. 파티에 god이 있으면 제낀다.
        for person in party_people:
            if person in gods:
                party_people.pop(party_people.index(person))
                break
            #5. 파티에 god이 없으면 answer 배열에 해당 파티를 추가한다.
            answer.append(party_people)

        #4. 제낌과 동시에 gods에 나머지 멤버도 추가한다. 
        # 이 때, 같은 사람의 중복 추가를 방지하기 위하여 gods를 집합으로 생성하였다.
        else:
            gods.add(person for person in party_people)
            continue


#2. 파티를 순회한다.
solution()
#6. 파티를 한번 더 순회한다.
solution()
#7. answer의 길이를 출력한다.
print(len(answer))

