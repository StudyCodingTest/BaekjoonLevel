# 단어 정렬하기
# 132ms
import sys
input = sys.stdin.readline
words = set()
for _ in range(int(input())): words.add(input().rstrip())
words = sorted(list(words), key=lambda word:(len(word),word))
print(*words, sep='\n')