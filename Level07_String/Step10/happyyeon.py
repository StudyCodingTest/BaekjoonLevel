# 문제 이름 : 그룹 단어 체커
# 문제 번호 : 1316
# 소요 시간 : 84ms

import sys

n = int(sys.stdin.readline()) # 단어의 개수
group_word_count = 0 # 그룹 단어 개수
for i in range(n) :
    word = sys.stdin.readline() # 단어
    for i in range(len(word)-1) :
        if (word[i] != word[i+1]) and (word[i+1:].find(word[i]) != -1) : # 연속된 문자열이 다른데, 그 문자가 뒤에서 또 발견되면
            break
    else :
        group_word_count += 1 # 안쪽 for문을 다 돌았는데도 break에 안 걸렸으면 그룹 단어인 경우임.
        continue # 바깥 for문은 마저 실행

print(group_word_count) 