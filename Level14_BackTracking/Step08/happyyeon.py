# 스타트와 링크
# 2784ms
from itertools import combinations
import sys
input = sys.stdin.readline
# 입력 조건
n = int(input())
fielders = [num for num in range(n)] # 선수 목록
ability_table = []
for _ in range(n) :
    ability_table.append(list(map(int,input().split()))) # 케미 능력치 테이블
differences_ability = [] # 능력치 차이
# 능력치 총합 구하기
def get_ability(fielders) :
    ability = 0
    for i in range(n//2) :
        for j in range(n//2) :
            ability += ability_table[fielders[i]][fielders[j]]
    return ability

cases_team = list(combinations(fielders,n//2)) # 선수 조합들

for idx in range(len(cases_team)//2) :
    start_team = list(cases_team[idx]) # 스타트 팀
    link_team = list(set(fielders) - set(start_team)) # 링크 팀
    differences_ability.append(abs(get_ability(start_team) - get_ability(link_team)))

print(min(differences_ability))


