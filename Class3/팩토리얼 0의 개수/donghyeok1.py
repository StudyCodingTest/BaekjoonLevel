import sys

def fact(N):
    # if N == 1:
    #     return 1
    # else:
    #     return N * fact(N - 1)
    result = 1
    for i in range(N):
        result *= (i+1)
    return result

#500까지 recursion 하면 recursive error 가 뜬다.
#걍 for문 써서 하면 됨.
        
    
N = int(sys.stdin.readline())
a = fact(N)
count = 0
while True:
    if a % 10 == 0:
        a = a // 10
        count += 1
    else:
        print(count)
        break