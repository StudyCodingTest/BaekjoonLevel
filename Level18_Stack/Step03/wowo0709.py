# 괄호
# 120ms
for _ in range(int(input())):
    s = 0
    for p in input():
        if p == '(': s += 1
        else: s -= 1
        if s < 0: break
    if s == 0: print('YES')
    else: print('NO')
        