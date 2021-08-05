# 문제 이름 : 설탕 배달
# 문제 번호 : 2839
# 소요 시간 : 72ms

import sys

n = int(sys.stdin.readline()) 

five_kg , remainder = divmod(n,5) # 5kg 봉투 개수

three_kg , another_remainder = divmod(remainder, 3) # 3kg 봉투 개수

# n -> 5 * five_kg + x --> 나머지가 3의 배수가 아니라면
    # 5 * (five_kg - 1) + x' --> 나머지가 3의 배수가 아니라면
    # 5 * (five_kg - 2) + x'' --> 5kg 봉투 개수를 계속 줄여가며 나머지가 3kg 봉투로 채울 수 있는지 확인
    # 그러다가 5kg 봉투가 -1에 도달하면 그 수는 5kg, 3kg로 나누어 떨어지지 않는 수

while another_remainder != 0 : 
    five_kg -= 1
    three_kg, another_remainder = divmod((n - 5 * five_kg), 3) 

if five_kg >= 0: 
    print(five_kg + three_kg)
else :
    print(-1)