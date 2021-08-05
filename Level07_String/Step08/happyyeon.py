# 문제 이름 : 다이얼
# 문제 번호 : 5622
# 소요 시간 : 80ms

import sys

word_dial = sys.stdin.readline() # 단어 주어짐
time_sum = 0 # 총 걸린 시간 초기화
seven_alphabet = ["P", "Q", "R", "S"]   # 한 다이얼 당 알파벳이 4개 포함되어 있는 경우
eight_alphabet = ["T", "U", "V"]  
nine_alphabet = ["W", "X", "Y", "Z"]
for i in range(len(word_dial)-1) :
    word_to_ascii = ord(word_dial[i]) # 알파벳 -> 숫자
    if word_to_ascii <= 79 : # 한 다이얼 당 알파벳이 3개만 존재하는 경우
        number_dial = int((word_to_ascii - 65) / 3) + 2 # 알파벳 -> 숫자
        time_sum += (number_dial - 1) + 2 # 1에는 문자가 없음.
    elif word_dial[i] in seven_alphabet : # P,Q,R,S
        time_sum += 8
    elif word_dial[i] in eight_alphabet : # T,U,V
        time_sum += 9
    elif word_dial[i] in nine_alphabet : # W,X,Y,Z
        time_sum += 10

print(time_sum)