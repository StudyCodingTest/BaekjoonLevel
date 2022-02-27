N, r, c = map(int,input().split())
i, j = 2**N//2, 2**N//2
cnt = 0
while N:
    if i > r: 
        i -= 2**N//4
        pass
    else: 
        i += 2**N//4
        cnt += (2**N//2)**2 * 2
    if j > c: 
        j -= 2**N//4
        pass
    else: 
        j += 2**N//4
        cnt += (2**N//2)**2
    N -= 1

print(cnt)