# 직각삼각형
# 80ms
while True:
    s = list(map(int,input().split()))
    if sum(s) == 0: break
    s.sort()
    print('right' if s[2]**2 == s[0]**2 + s[1]**2 else 'wrong')
