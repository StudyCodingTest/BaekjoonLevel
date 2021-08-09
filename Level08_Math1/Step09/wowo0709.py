# Fly me to the Alpha Centauri
# 80ms
for _ in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x
    root = int(dist**(1/2)) # 제곱수 ~ 다음 제곱수-1 이 한 그룹

    if dist < 4: ans = dist
    elif dist == root ** 2: ans = 2 * root - 1
    elif root ** 2 < dist <= root ** 2 + root: ans = 2 * root
    elif dist > root ** 2 + root: ans = 2 * root + 1
    print(ans)




