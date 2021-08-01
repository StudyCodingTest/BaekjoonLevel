# 문제: 평균의 넘겠지
# 시간: 72ms
import sys
input = sys.stdin.readline

C = int(input())
answer = [0 for _ in range(C)]
for i in range(C):
    line = list(map(int,input().split()))
    N,scores = line[0],line[1:]
    ave = sum(scores)/N
    for score in scores:
        if score > ave: answer[i] += 100 # 백분율
    answer[i] /= N

for a in answer:
    print("{:.3f}".format(a)+'%')