# 베르트랑 공준
# 2380ms
isPrime = [False, False]
while True:
    n = int(input())
    if n == 0: break
    if 2*n+1 > len(isPrime): isPrime += [True] * (2*n+1-len(isPrime)) # 재활용
    for i in range(2, int((2*n)**(1/2))+1):
        if not isPrime[i]: continue
        for j in range(2*i, 2*n+1, i):
            isPrime[j] = False

    print(len([num for num in range(n+1,2*n+1) if isPrime[num]]))