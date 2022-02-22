# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline

# Á¶°Ç
target = int(input())
num_wrong = int(input())

if num_wrong:
    wrongs = list(input().split())
else:
    wrongs = []

answer = abs(target-100)

for i in range(1000001):
    for a in str(i):
        if a in wrongs:
            break
    else:
        answer = min(answer,len(str(i))+abs(target-i))

print(answer)