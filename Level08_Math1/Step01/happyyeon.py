# 문제 이름 : 손익분기점
# 문제 번호 : 1712
# 소요 시간 : 72ms

import sys

a,b,c = map(int, sys.stdin.readline().split()) # A,B,C 입력 받음

if b >= c : # b=c이면 zero division error , b-c>0 이면 a >0이므로 손익분기점이 - 
    print(-1) 
else :
    print(int(-a / (b-c)) + 1) # 손익분기점