# 백준 - 1043 , 2트
import sys
input = sys.stdin.readline

# 초기 구성
cnt_person, cnt_party = map(int,input().split())
witness_set = set(map(int,input().split()[1:]))
possible_lie = [1]*cnt_party
party_list = []
for i in range(cnt_party):
    party_list.append(set(map(int,input().split()[1:])))

# https://itholic.github.io/kata-1043/ [참고]
for i in range(cnt_party):
    for idx,party in enumerate(party_list):
        if witness_set.intersection(party):
            possible_lie[idx] = 0
            witness_set = witness_set.union(party)

print(sum(possible_lie))


