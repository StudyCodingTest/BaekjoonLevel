# 문제 이름 : 소수
# 문제 번호 : 2581
# 소요 시간 : 440ms

import sys

# 문제에 필요한 변수들
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
prime_nums = [] 
# # 소수 판별 함수 
def checkPrimeNum(num) :  
    if num == 1:
        return 0
    else :
        for devider in range(2,num) :
            if num % devider == 0 :
                return 0
        
        return 1

# M~N 소수 리스트 생성
for num in range(m, n+1) :
    if checkPrimeNum(num) == 1 :
        prime_nums.append(num)

# 소수 합, 최소 소수 출력
if not prime_nums :
    print(-1)
else :
    print(sum(prime_nums), min(prime_nums), end="\n")