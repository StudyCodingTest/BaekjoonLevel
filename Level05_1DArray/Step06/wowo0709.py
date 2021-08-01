# 문제: OX 퀴즈
# 시간: 76 ms
import sys
input = sys.stdin.readline

scores = []
for _ in range(int(input())):
    scoreList = [0] + list(input()) # 맨 앞에 더미값 0
    for i in range(1,len(scoreList)):
        scoreList[i] = scoreList[i-1] + 1 if scoreList[i] == 'O' else 0
    scores.append(sum(scoreList))

for score in scores:
    print(score)