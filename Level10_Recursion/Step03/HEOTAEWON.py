#문제: 별 찍기 - 10
#번호: 2447
#시간: 116ms


import sys


def pattern(stars):
    matrix = []
    for i in range(3*len(stars)): # 3일때는 9번 반복
        if i // len(stars) == 1: # 가운데에 빈칸 만들기
            # 현재 len(stars)는 3으로 나눠진 값으로 생각할 수 있기 때문에 공백을 그만큼 넣고 나머지만큼 더해줌
            matrix.append(stars[i%len(stars)] + ' '*len(stars) + stars[i%len(stars)])
        else:
            matrix.append(stars[i%len(stars)] * 3)
    return matrix


n = int(sys.stdin.readline())
stars = ['***', '* *', '***'] # 초기 시작
e = 0 # 지수
while n!= 3:
    e += 1
    n //= 3

for i in range(e): # e번만큼 반복
    stars = pattern(stars)
for i in stars:
    print(i)
