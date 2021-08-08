# 문제 이름 : 소수 찾기
# 문제 번호 : 1978
# 소요 시간 : 72ms

import sys

# 문제에 필요한 변수들
n = int(sys.stdin.readline()) 
nums = list(map(int,sys.stdin.readline().split())) # 입력 각 자리 숫자들 --> 리스트에 삽입
prime_num_count = 0 # 총 소수 개수
# 소수 판별 함수
def checkPrimeNum(num) :  
    if num == 1:
        return 0
    else :
        for devider in range(2,num) :
            if num % devider == 0 :
                return 0
        
        return 1
# 리스트 순회하며 소수 개수 체크
for i in range(len(nums)) :
    prime_num_count += checkPrimeNum(nums[i])

print(prime_num_count)


    


