# 문제 이름 : 골드바흐의 추측
# 문제 번호 : 9020
# 소요 시간 : 1920ms

import sys

all_nums = [num for num in range(1,10001)] # 전체 숫자 리스트
prime_nums = [] # 소수 리스트
def checkPrimeNum(num) :  # 소수 판별 함수
    if num == 1:
        return 0
    for devider in range(2, int(num**0.5)+1) :
        if num % devider == 0 :
            return 0
    
    return 1

# 소수 추출
for num in all_nums :
    if checkPrimeNum(num) :
        prime_nums.append(num)

for i in range(int(sys.stdin.readline())) : # 테스트 케이스
    n = int(sys.stdin.readline()) # 인풋
    std_num = n // 2 # 기준 숫자

    while True :
        if std_num in prime_nums and n - std_num in prime_nums : # N = A+B, A와 B가 모두 소수일 때
            print(n-std_num, std_num) # 오름차순으로 프린트
            break
        std_num += 1

