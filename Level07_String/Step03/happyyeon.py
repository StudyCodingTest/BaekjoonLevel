# 문제 이름 : 알파벳 찾기
# 문제 번호 : 10809
# 소요 시간 : 92ms

import sys

s = sys.stdin.readline() # 단어 S를 입력 받음

alphabet_location = [-1 for i in range(26)] # 알파벳 위치를 저장할 리스트 생성 및 초기화

for i in reversed(range(len(s)-1)) : # S의 길이만큼 하나씩 돌면서 알파벳 위치를 지정한다. 단 \n은 제외하기 위해 -1
    alphabet_location[ord(s[i]) - 97] = i  # 아스키 코드 a = 97

for i in range(26) : # 공백을 기준으로 알파벳 위치 리스트의 각 원소들을 출력
    print(alphabet_location[i], end=" ")