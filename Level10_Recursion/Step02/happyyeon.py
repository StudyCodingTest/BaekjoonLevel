# 피보나치 수 5
# 84ms

import sys

def get_fibonacci(num) : # n번째 피보나치 수
    if num == 0 :
        return 0
    if num == 1 :
        return 1
    
    return get_fibonacci(num-1) + get_fibonacci(num-2)

print(get_fibonacci(int(sys.stdin.readline())))