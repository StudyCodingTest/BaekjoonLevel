#문제: 영화감독 숌
#시간: 884ms


import sys


n = int(sys.stdin.readline())
count = 0 # 몇번째인지 카운트
m = 666 # 첫번째 666부터 시작
while True:
    if '666' in str(m): # 문자열 형태로 변환 후 '666'이 있는지 확인
        count += 1 # 있다면 카운트
        if count == n: # n번째 숫자가 등장하면 출력 후 break
            print(m)
            break
    m += 1 # n번째 숫자가 등장할 때까지 증가
