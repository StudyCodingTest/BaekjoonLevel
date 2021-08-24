#문제: 단어 정렬
#시간: 1168ms


import sys


words = [] # 단어들을 저장할 리스트
for _ in range(int(sys.stdin.readline())):
    word = input() # 단어를 입력받음
    word_lengh = len(word) # 단어의 길이를 저장
    words.append((word, word_lengh)) # 튜플형태로 단어와 단어의 길이를 리스트에 저장

words = list(set(words)) # set으로 변환하고 다시 list로 변환하여 중복제거
words.sort(key=lambda x: (x[1], x[0])) # 1. 길이 순, 2. 알파벳 순 으로 정렬
for word in words: # 단어만 출력
    print(word[0])
