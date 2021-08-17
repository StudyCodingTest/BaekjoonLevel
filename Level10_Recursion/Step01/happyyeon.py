# 팩토리얼
# 80ms

import sys

def get_factorial(num) :  # N!
    if num == 0 or num == 1 :
        return 1

    return num * get_factorial(num-1)

print(get_factorial(int(sys.stdin.readline()))) 


