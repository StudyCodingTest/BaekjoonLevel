# 피보나치 함수
# 80ms
def fibonacci(n):
    global fibos
    if n in fibos:
        return fibos[n]
    fibos[n] = list(map(sum,zip(fibonacci(n-1),fibonacci(n-2))))
    return fibos[n]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

fibos = {0: [1,0], 1: [0,1]}
for _ in range(int(input())):
    print(*fibonacci(int(input())))