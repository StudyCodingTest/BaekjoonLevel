# 문제 이름 : 단어 공부
# 문제 번호 : 1157
# 소요 시간 : 348ms

import sys
# 문자열 입력이 addb라고 가정
word = sys.stdin.readline().upper() # 입력된 문자열을 대문자로 변경

alphabet = [0 for i in range(26)] # 알파벳 리스트 생성 및 초기화

for i in range(len(word)-1) :  # 아스키 코드 a = 65 , 알파벳 리스트에 a,b,c,d ... 단어 사용 빈도 카운트
    alphabet[ord(word[i]) - 65] += 1

max_count = max(alphabet)
twice_check = alphabet.count(max_count)
if twice_check > 1 :  # 제일 많이 사용한 단어가 1개 초과 일 때
    print("?")

elif twice_check == 1 : # 제일 많이 사용한 단어가 유일할 때
    print(chr(alphabet.index(max_count) + 65)) # 제일 많이 사용한 단어의 인덱스(아스키 코드)를 받아와서 알파벳으로 변환