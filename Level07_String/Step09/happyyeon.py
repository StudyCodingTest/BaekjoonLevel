# 문제 이름 : 크로아티아 알파벳
# 문제 번호 : 2941
# 소요 시간 : 84ms

import sys

transfer_alphabet = sys.stdin.readline() # 변경된 알파벳 입력 받음

transfer_list = ["c=", "c-", "d-", "lj", "nj", "s=", "z="] # 변경 알파벳 리스트 생성
word_count = 0 

word_length = len(transfer_alphabet) # Time Complexity 감소를 위하여 len 함수를 한 번만 사용
i = 0
while i <= word_length - 2 : # 단어의 길이와 인덱스 마지막 번호는 1 차이가 남, 인풋 받을때 \n이 딸려옴. --> -2를 빼줌
    if transfer_alphabet[i:i+2] in transfer_list : # 연속된 2개의 글자가 1 단어일 때
        word_count += 1
        i += 2
    elif transfer_alphabet[i:i+3] == "dz=" : # 연속된 3개의 글자가 1 단어일 때
        word_count += 1
        i += 3
    else : # 일반 알파벳일 때
        word_count += 1
        i += 1

print(word_count)


