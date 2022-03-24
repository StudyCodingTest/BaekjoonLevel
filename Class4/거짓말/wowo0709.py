'''
거짓말을 들킬 경우
1. 진실을 알고 있는 사람이 거짓말을 들을 경우
2. 어떤 사람이 어떤 파티에서는 진실을 듣고 다른 파티에서는 거짓말을 들을 경우
풀이 순서
1. 진실을 알고 있는 사람이 많은 순으로 내림차순 정렬
2. 위에서부터 진실을 말하면서 새롭게 진실을 들은 사람들을 knowns에 추가
3. 진실을 알고 있는 사람이 없을 때까지 1~2 반복
'''
N, M = map(int,input().split())
knowns = set(list(map(int,input().split()))[1:])
parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party+[sum([person in knowns for person in party])]) # [사람1, 사람2, ..., 진실을 알고 있는 사람수]

from collections import deque
while True:
    parties = deque(sorted(list(parties),key=lambda x:x[-1], reverse=True))
    if not parties or parties[0][-1] == 0:
        break
    new_knowns = set()
    while parties and parties[0][-1] != 0:
        party = parties.popleft()
        new_knowns |= set([person for person in party[:-1] if person not in knowns])

    knowns = new_knowns
    for i in range(len(parties)):
        parties[i][-1] = sum([person in knowns for person in parties[i]])

print(len(parties))
    

