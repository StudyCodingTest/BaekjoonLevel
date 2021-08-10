# 골드바흐의 추측
# 4448ms
isPrime = [False, False]
for _ in range(int(input())):
    n = int(input())
    if n > len(isPrime): isPrime += [True] * (n+1-len(isPrime)) # 재활용
    for i in range(2, int(n**(1/2))+1):
        if not isPrime[i]: continue
        for j in range(2*i, n+1, i):
            isPrime[j] = False

    for num in range(n//2, 1, -1):
        if isPrime[num] and isPrime[n-num]:
            print(num, n-num)
            break