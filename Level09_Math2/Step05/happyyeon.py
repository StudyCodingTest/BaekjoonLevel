# 문제 이름 : 베르트랑 공준
# 문제 번호 : 4948
# 소요 시간 : 1648ms

import sys

# 소수 판별 함수
def checkPrimeNum(num) :  
    if num == 1:
        return 0
    for devider in range(2, int(num**0.5)+1) :
        if num % devider == 0 :
            return 0
    
    return 1

all_nums = [num for num in range(1,246913)] # 전체 숫자 리스트
prime_nums = [] # 소수 리스트

# 전체 리스트에서 소수만 추출
for num in all_nums :
    if checkPrimeNum(num) :
        prime_nums.append(num)

while True :
    n = int(sys.stdin.readline())
    count = 0
    if n == 0 :
        break
    for num in prime_nums :
        if n < num <= 2*n :
            count += 1

    
    print(count)
