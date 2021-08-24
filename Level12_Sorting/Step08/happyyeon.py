# 단어 정렬
# 1148ms

import sys

words = []

# 인풋 단어 리스트에 추가
for i in range(int(sys.stdin.readline())) :
    words.append(input())

# 같은 단어 제거
words = list(set(words))

# 길이와 알파벳 순 정렬
words.sort(key=lambda item : (len(item), item))
# 결과 출력
for word in words :
    print(word)
             
