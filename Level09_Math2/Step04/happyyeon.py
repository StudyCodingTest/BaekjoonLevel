# 문제 이름 : 소수 구하기
# 문제 번호 : 1929
# 소요 시간 : 2424ms

import sys

m,n = map(int, sys.stdin.readline().split())

# 1 --> 소수, 0 --> 소수X
bool_prime_nums = [1 for i in range(n+1)]
bool_prime_nums[0:2] = [0, 0]

for i in range(2,n+1) :
    for j in range(2, (n//i)+1) :
        bool_prime_nums[i*j] = 0


prime_nums = [i for i, value in enumerate(bool_prime_nums) if value == 1 and i >= m]

print(*(prime_nums), sep="\n")
     




