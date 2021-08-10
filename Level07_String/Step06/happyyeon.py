# 문제 이름 : 단어의 개수
# 문제 번호 : 1152
# 소요 시간 : 88ms

import sys

string = sys.stdin.readline() # 문자열 입력 받음

string_list = string.split() # 공백을 기준으로 문자열 생성

print(len(string_list)) 