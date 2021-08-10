#문제: 소인수분해
#번호: 11653
#시간: 1632ms

N = int(input())
divide = 2 #2부터 나누기 시작

while N != 1: #N이 나눠지고 마지막 1이 될때까지 반복
    if N%divide == 0: #나눌 수 있다면 나눈 후 출력
        N /= divide
        print(divide)
    else: #나눌 수 없다면 1씩 증가
        divide += 1
